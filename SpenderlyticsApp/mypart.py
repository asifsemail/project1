from mycalcs import mycalc
import plotly.graph_objects as go
def generatefigure1():
    generatefigure1.fig = go.Figure()
    generatefigure1.fig.add_trace(
        go.Scatter(x=mycalc.totalspendperday.index, y=mycalc.totalspendperday["TotalSpent"], mode="lines", name="All Customers",
                   line=dict(color="blue", width=2)))
    generatefigure1.fig.add_trace(go.Scatter(x=mycalc.topltvcustomers_groupby.index, y=mycalc.topltvcustomers_groupby["totalspend"], mode="lines",
                             name="Top 25% LTV Customers", line=dict(color="orange", width=2)))
    generatefigure1.fig.update_layout(title="All Customers vs. Top 25% LTV Customers Total Spending per Day", xaxis_title="Date",
                      yaxis_title="Amount Spent ($)", showlegend=True)
    generatefigure1.fig.show()

def generatefigure2():
    generatefigure2.fig = go.Figure()
    generatefigure2.fig.add_trace(
        go.Scatter(x=mycalc.topltvcustomers_groupby.index, y=mycalc.topltvcustomers_groupby["totalspend"], mode="markers",
                       name="Top 25% LTV Customers", marker=dict(symbol="circle", color="blue", size=5)))
    generatefigure2.fig.add_trace(go.Scatter(x=mycalc.forecast_df.index, y=mycalc.forecast_df["yhat"], mode="lines", name="Prediction",
                                 line=dict(color="orange", width=2)))
    generatefigure2.fig.add_trace(go.Scatter(x=mycalc.forecast_df_lower.index, y=mycalc.forecast_df_lower["yhat_lower"], mode="lines",
                                 name="Prediction Lower", line=dict(color="red", width=.25)))
    generatefigure2.fig.add_trace(go.Scatter(x=mycalc.forecast_df_upper.index, y=mycalc.forecast_df_upper["yhat_upper"], mode="lines",
                                 name="Prediction Upper", line=dict(color="green", width=.25)))

    generatefigure2.fig.update_layout(title="Forecast of Top 25% LTV Customers", xaxis_title="Date", yaxis_title="Amount Spent ($)",
                          showlegend=True)
    generatefigure2.fig.update_yaxes(range=[0, 250000])

    generatefigure2.fig.show()

def generatefigure3():
    generatefigure3.fig = go.Figure()
    generatefigure3.fig.add_trace(go.Scatter(x=mycalc.ss.index, y=mycalc.ss["totalspend"], mode="lines", name="Top 25% LTV Customers",
                             line=dict(color="blue", width=2)))
    generatefigure3.fig.add_trace(go.Scatter(x=mycalc.ss.index, y=mycalc.ss["predictedspend"], mode="lines", name="Prediction",
                             line=dict(color="orange", width=2)))

    generatefigure3.fig.update_layout(title="Forecast of Top 25% LTV Customers", xaxis_title="Date", yaxis_title="Amount Spent ($)",
                      showlegend=True)
    generatefigure3.fig.update_yaxes(range=[0, 250000])
    generatefigure3.fig.show()
