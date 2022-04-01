import pandas as pd
from prophet import Prophet

import matplotlib.pyplot as plt

# Optional parser lambda to parse months
df = pd.read_csv('src/alameda.csv', parse_dates=['Date'], date_parser=lambda x:pd.to_datetime(x, format='%Y%m'))
# print(df.head())

df1 = df[['Date', 'Value']]
df1 = df1.rename(columns={'Date': 'ds', 'Value': 'y'})
print(df1.head())

m = Prophet()
m.fit(df1)

future = m.make_future_dataframe(periods=365)
# print(future.tail())

forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# print(help(Prophet.fit))


fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)

plt.show()

