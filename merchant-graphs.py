# # -*- coding: utf-8 -*-
# """Copy of Untitled1.ipynb

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1eDfKwSP0vvg_QTqZQMHN1EdduOXesd4o
# """

# !pip install hvplot

# dependencies .. lets put all the dependencies here
import pandas as pd
#from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os
import numpy as np
import datetime as dt
import hvplot.pandas as hv
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import math

import panel as pn

pn.extension()

global data
data = None

def read_csv():
  global data
  if data == None:
    data = pd.read_csv('credit_card_transactions.csv')
  return data.copy()

df_transactions = read_csv()
df_transactions.head()

df_merchants = df_transactions[['trans_date_trans_time','cc_num','merchant','category','amt','city','state','zip','city_pop','job','dob','merch_zipcode']]
df_merchants.head()

df_merchants['transaction_datetime'] = pd.to_datetime(df_merchants['trans_date_trans_time'])

df_merchants.drop(columns=['trans_date_trans_time'], inplace=True)
df_merchants.head()

df_merchants['merchant'] = df_merchants['merchant'].apply(lambda x: x.strip('fraud_'))
df_merchants.head()

df_merchant_summary = df_merchants.groupby(['merchant']).agg(total_sales = ('amt','sum')).sort_values(by='total_sales', ascending=False)
df_merchant_summary.head()

print("Plot-1")
df_merchant_top10 = df_merchant_summary.head(10)
plot_merchant_summary_up = df_merchant_top10.hvplot.bar(rot=45, x='merchant', y='total_sales', ylim=(0, 500000), height=500, width=800)
plot_merchant_summary_up.opts(title='TOP 10 Selling Merchants (entire duration)', xlabel='Merchants', ylabel='Total Sales')
plot_merchant_summary_up



print("Plot-2")
df_merchant_bottom10 = df_merchant_summary.tail(10)
plot_merchant_summary_down = df_merchant_bottom10.hvplot.bar(rot=45, x='merchant', y='total_sales', ylim=(0, 60000), height=500, width=800)
plot_merchant_summary_down.opts(title='10 Least Selling Merchants (entire duration)', xlabel='Merchants', ylabel='Total Sales')
plot_merchant_summary_down

df_merchants.set_index('transaction_datetime', inplace=True)
df_merchants.head(5)

df_merchant_category_summarized = df_merchants.groupby(by = [df_merchants.index.year, df_merchants.index.quarter, 'merchant']).agg(total_sales = ('amt','sum'))

df_merchant_sales_for_quarter = df_merchant_category_summarized.sort_values(by=['total_sales'], ascending=False)

print("Plot-3")

plot_merchant_sales_for_quarter_top10 = df_merchant_sales_for_quarter.head(10).hvplot(kind='bar', rot=45 ,xlabel='Year-Quarter-Merchant', ylabel= 'Total Sale for Quarter/Merchant', title ='Top 10 Sale for Merchant Quarter combination' ,figsize=(10,5))

print("Plot-4")

plot_merchant_sales_for_quarter_bottom10 = df_merchant_sales_for_quarter.tail(10).hvplot(kind='bar', xlabel='Year-Quarter-Merchant', rot=45, ylabel= 'Total Sale for Quarter/Merchant', title ='10 Least Sale for Merchant Quarter combination' ,figsize=(10,5))

df_sales = df_merchants[['amt']]
df_sales['days_in_months'] = df_sales.index.days_in_month
df_sales['year'] = df_sales.index.year

df_sales_yearwise = df_sales.groupby(by = [df_sales.index.month]).agg(
    total_sales_month = ('amt','sum'),
    count_transactions = ('amt','count'),
    days_in_months = ('days_in_months','mean'),
    avg_sales_month = ('amt','mean'),
    max_year = ('year','max'),
    min_year = ('year','min')
    )

df_sales_yearwise.index.names = ['month']
df_sales_yearwise['avg_sales_per_month'] = df_sales_yearwise['total_sales_month']/((df_sales_yearwise['max_year']-df_sales_yearwise['min_year'])+1)
df_sales_yearwise['avg_transaction_per_month'] = df_sales_yearwise['count_transactions']/((df_sales_yearwise['max_year']-df_sales_yearwise['min_year'])+1)

nos_of_merchants = len(df_merchants['merchant'].unique())

df_sales_yearwise['sales/month/customer'] = df_sales_yearwise['avg_sales_per_month']/nos_of_merchants
df_sales_yearwise['transaction/month/customer'] = df_sales_yearwise['avg_transaction_per_month']/nos_of_merchants

df_sales_yearwise_copy = df_sales_yearwise[['sales/month/customer','transaction/month/customer']]
df_sales_yearwise_copy

# fig, (ax1, ax2) = plt.subplots(1,2, figsize=(8,4))

# fig.suptitle('Average transactions in one year per merchant')
# ax1.set_title('Average number of transaction/month/customer')
# ax2.set_title('Average sales/month/customer')
# print("Plot-5")

#plot_sales_month_customer = ax1.plot(df_sales_yearwise_copy.index, df_sales_yearwise_copy['sales/month/customer'], label='sales/month/customer', )
plot_sales_month_customer = df_sales_yearwise_copy.hvplot()
#plot_transaction_month_customer = ax2.plot(df_sales_yearwise_copy.index, df_sales_yearwise_copy['transaction/month/customer'], label='transaction/month/customer')
#plot_sales_month_customer
#plot_transaction_month_customer

df_merchants_bottom = df_merchants.loc[df_merchants['merchant'].isin([x for x in df_merchant_bottom10.index])]
df_merchants_sales_bottom_pvt = pd.pivot_table(df_merchants_bottom, values='amt', index=[df_merchants_bottom.index.month], columns ='merchant', aggfunc='sum')

print("Plot-6")

plot_merchants_sales_bottom_pvt = df_merchants_sales_bottom_pvt.hvplot(kind='line', xlabel='Months', rot=45, ylabel= 'Merchant', title ='10 Least Sale for Merchant over year' ,figsize=(20,10))

df_merchants_cnt_trans_bottom_pvt = pd.pivot_table(df_merchants_bottom, values='amt', index=[df_merchants_bottom.index.month], columns ='merchant', aggfunc='count')

print("Plot-7")

plot_merchants_cnt_trans_bottom_pvt = df_merchants_cnt_trans_bottom_pvt.hvplot(kind='line', xlabel='Months', rot=45, ylabel= 'Merchant', title ='Nos of transaction for 10 Least Sale for Merchant over year' )

df_merchants_top = df_merchants.loc[df_merchants['merchant'].isin([x for x in df_merchant_top10.index])]
df_merchants_sales_top_pvt = pd.pivot_table(df_merchants_top, values='amt', index=[df_merchants_top.index.month], columns ='merchant', aggfunc='sum')
print("Plot-8")

plot_merchants_sales_top_pvt = df_merchants_sales_top_pvt.hvplot(kind='line', xlabel='Months', rot=45, ylabel= 'Merchant', title ='10 Top Selling Merchants over year')

df_merchants_cnt_trans_top_pvt = pd.pivot_table(df_merchants_top, values='amt', index=[df_merchants_top.index.month], columns ='merchant', aggfunc='count')

print("Plot-9")
plot_merchants_cnt_trans_top_pvt = df_merchants_cnt_trans_top_pvt.hvplot(kind='line', xlabel='Months', rot=45, ylabel= 'Merchant', title ='Nos of transactions for 10 Top Selling Merchant for year' )

df_merchant_summary['quartile'] = pd.qcut(df_merchant_summary['total_sales'], q=4, labels=False)

quantile = df_merchant_summary['total_sales'].quantile([0.25,0.5,0.75])

iqr = quantile.loc[0.75] - quantile.loc[0.25]
upperbound = quantile.loc[0.5] + (1.5 * (iqr))
lowerbound = quantile.loc[0.5] - (1.5 * (iqr))

print(f'Merchant wise sale details:')
print(f'Upperbound: {upperbound} Lowerbound: {lowerbound} Median: {quantile.loc[0.5]} IQR: {iqr}')

df_quartiles = df_merchant_summary.groupby('quartile').agg(quartitle_sales = ('total_sales','sum'), count_merchants=('quartile','count'))

"""Calculating 75 %tile sales merchants"""

fig, (ax1) = plt.subplots(1)
_wedges, labels, percentages = ax1.pie(df_quartiles['quartitle_sales'], labels=df_quartiles.index, autopct='%1.1f%%', counterclock=False,
                                       startangle=90)
percentiles = [x*25 for x in range(0, 5, 1)]
i = 0
for label, percentage in zip(labels, percentages):
    label.set_text('Quartile ' + str(i+1) + '\n' + str(percentiles[i]) + '-' + str(percentiles[i+1]) + '%')
    amount = df_quartiles.iloc[i]['quartitle_sales']
    percentage.set_text(f'${amount:,.2f}\n{str(percentage.get_text())}')
    i += 1

total_sales = df_quartiles['quartitle_sales'].sum()
plt.title(f'Merchant sales quartiles - Total Sales for entire duration : ${total_sales:,.2f}')

plt.legend(loc='upper left')
plt.show()

print("Plot-10")


df_merchant_state = df_merchants[['merchant','category','amt','state']]

df_merchant_state_quarterly = df_merchant_state.groupby(by = ['merchant','state',df_merchant_state.index.year ,df_merchant_state.index.quarter]).agg(total_sales = ('amt','sum'))
df_merchant_state_quarterly.index.names = ['merchant','state','year','quarter']
df_merchant_state_quarterly = df_merchant_state_quarterly.sort_values (by='total_sales', ascending=False)
df_merchant_state_quarterly.head(10).plot(kind='bar', rot=90 ,xlabel='Year-Quarter-Merchant-State', ylabel= 'Total Sale for Quarter/Merchant', title ='Top 10 Sale for Merchant Quarter State combination' ,figsize=(8,4))

df_merchant_state_quarterly.tail(10).plot(kind='bar', rot=90 ,xlabel='Year-Quarter-Merchant-State', ylabel= 'Total Sale for Quarter/Merchant statewise', title ='Lowest 10 Sale for Merchant Quarter State combination' ,figsize=(8,4))

df_merchant_statewise = df_merchant_state.groupby(by = ['merchant','state']).agg(total_sales = ('amt','sum')).sort_values(by='total_sales', ascending=False)
df_merchant_statewise.head(10)

df_merchant_statewise_top10 = df_merchant_statewise.head(10)
df_merchant_statewise_top10.index.names = ['merchant','state']
print("Plot-11")

plot_merchant_statewise_top10 = df_merchant_statewise_top10.hvplot(kind='bar', rot=45, x='merchant', by='state', y='total_sales', ylim=(0, 40000), title='TOP 10 Merchant State combination sales' ,height=500, width=1500)
plot_merchant_statewise_top10

df_merchant_statewise_bottom10 = df_merchant_statewise.tail(10)
df_merchant_statewise_bottom10.index.names = ['merchant','state']

print("Plot-12")

plot_merchant_statewise_bottom10 = df_merchant_statewise_bottom10.hvplot(kind='bar', rot=45, x='merchant', by='state', y='total_sales', ylim=(0, 2), title='Least 10 Merchant State combination sales',legend='top_right' ,height=500, width=1500)
plot_merchant_statewise_bottom10

pn.serve({
      'top_10_merchants':plot_merchant_summary_up,
      'bottom_10_merchants':plot_merchant_summary_down,
      'quarter_top_10_merchants':plot_merchant_sales_for_quarter_top10,
      'quarter_bottom_10_merchants':plot_merchant_sales_for_quarter_bottom10,
      'avg_sales_merchants_year': plot_sales_month_customer,
      'avg_transactions_merchants_year': plot_sales_month_customer,
      'Ten_Least_selling_merchants_sales_year': plot_merchants_sales_bottom_pvt,
      'Ten_Least_selling_merchants_transactions_year': plot_merchants_cnt_trans_bottom_pvt,
      'Ten_Most_selling_merchants_transactions_year': plot_merchants_sales_top_pvt,
      'Ten_Most_selling_merchants_sales_year': plot_merchants_cnt_trans_top_pvt,
      #'Merchant_sales_quartiles_duration': plt,
      'Statewise_sales_top_10_merchants': plot_merchant_statewise_top10,
      'Statewise_sales_top_10_merchants': plot_merchant_statewise_bottom10
      })
