from importdatafile import importdata
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
from prophet import Prophet


def mycalc():
    df = importdata.data.copy()
    df["trans_year"] = list(
        map(lambda x: x.split(" ")[0].split("-")[0], df["trans_date_trans_time"]))
    df["trans_month"] = list(
        map(lambda x: x.split(" ")[0].split("-")[1], df["trans_date_trans_time"]))
    df["trans_day"] = list(
        map(lambda x: x.split(" ")[0].split("-")[2], df["trans_date_trans_time"]))
    df["trans_date"] = list(map(lambda x: x.split(" ")[0], df["trans_date_trans_time"]))

    cc_nums = df["cc_num"].unique()
    numoftrans = df["Unnamed: 0"].count()
    numofrecenttrans = df[df["trans_date_trans_time"] > "2020-03-21"]["Unnamed: 0"].count()

    df3_merged = pd.concat([df.groupby("cc_num").agg(totaltransactions=("amt", "count")) / numoftrans,
                            df.groupby("cc_num").agg(totalspend=("amt", "sum")) / df["amt"].sum(),
                            df[df["trans_date_trans_time"] >= "2020-03-21"].groupby("cc_num").agg(
                                numberofrecenttransactions=("amt", "count")) / numofrecenttrans],
                           axis=1)
    df3_merged.rename(columns={"totaltransactions": "Total Transactions Ratio", "totalspend": "Total Spend Ratio",
                               "numberofrecenttransactions": "Total Recent Transactions Ratio (last 90 days)"},
                      inplace=True)

    ltv_df = pd.DataFrame(df3_merged, index=cc_nums)
    ltv_df["LTV Score"] = ltv_df["Total Transactions Ratio"] * .25 + ltv_df["Total Spend Ratio"] * .50 + ltv_df[
        "Total Recent Transactions Ratio (last 90 days)"] * .25
    ltv_df.sort_values(by="LTV Score", ascending=False, inplace=True)
    ltv_df["LTV Score"] = ltv_df["LTV Score"] / ltv_df["LTV Score"].max() * 100

    top25percentltv = ltv_df["LTV Score"].describe().iloc[6]
    ltv_top25percent = ltv_df[ltv_df["LTV Score"] >= top25percentltv]

    topltvcustomers = df.loc[df["cc_num"].isin(ltv_top25percent.index)]

    mycalc.totalspendperday = df.groupby("trans_date").agg(TotalSpent=("amt", "sum"))
    mycalc.topltvcustomers_groupby = topltvcustomers.groupby("trans_date").agg(totalspend=("amt", "sum"))

    prophet_df = mycalc.topltvcustomers_groupby.reset_index()

    prophet_df.columns = ['ds', 'y']
    prophet_df.head()

    m = Prophet()

    m.fit(prophet_df)
    future = m.make_future_dataframe(periods=365 * 3)
    forecast = m.predict(future)

    mycalc.forecast_df = pd.DataFrame(forecast["yhat"])
    mycalc.forecast_df.index = pd.date_range(start="2019-01-01", end="2023-06-20")

    mycalc.forecast_df_lower = pd.DataFrame(forecast["yhat_lower"])
    mycalc.forecast_df_lower.index = pd.date_range(start="2019-01-01", end="2023-06-20")

    mycalc.forecast_df_upper = pd.DataFrame(forecast["yhat_upper"])
    mycalc.forecast_df_upper.index = pd.date_range(start="2019-01-01", end="2023-06-20")

    train = mycalc.topltvcustomers_groupby.iloc[:]
    model = ARIMA(train["totalspend"], order=(2, 1, 3))
    model = model.fit()
    start=1
    end=538
    pred=model.predict(start=start,end=end,typ="levels")
    pred.index=pd.date_range(start="2020-01-01",end="2021-06-21")
    mycalc.ss = pd.concat([mycalc.topltvcustomers_groupby, pred])
    mycalc.ss.rename(columns={"predicted_mean": "predictedspend"}, inplace=True)
