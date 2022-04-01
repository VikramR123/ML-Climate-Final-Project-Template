import pandas as pd
from prophet import Prophet

import matplotlib.pyplot as plt

# Optional parser lambda to parse months
df = pd.read_csv('src/alameda.csv', parse_dates=['Date'], date_parser=lambda x:pd.to_datetime(x, format='%Y%m'))
# print(df.head())


df1 = df[['Date', 'Value']]
df1 = df1.rename(columns={'Date': 'ds', 'Value': 'y'})
print(df1.head())


# Add cap and floor
# df1['cap'] = 10
# df1['floor'] = 0


m = Prophet() # Defaults to linear growth
# m = Prophet(growth='logistic')
m.fit(df1)


# TESTING Rolling mean
df1.y = df1.y.rolling(window=6).mean()


future = m.make_future_dataframe(periods=36, freq='MS')
# Add cap and floor for logistic
# future['cap'] = 10
# future['floor'] = 0
# print(future.tail())

forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# print(help(Prophet.fit))


fig1 = m.plot(forecast)

# Rolling mean
windowSize = 6
plt.plot(df1.ds, df1.y.rolling(window=windowSize).mean(), color="red")
# Rolling stddev
plt.plot(df1.ds, df1.y.rolling(window=windowSize).std(), label="rolling std (x10)", color="green")

plt.plot(forecast.ds[-(36+windowSize):], forecast.yhat[-(36+windowSize):].rolling(window=windowSize).mean(), color="purple")

# fig2 = m.plot_components(forecast)

plt.show()

