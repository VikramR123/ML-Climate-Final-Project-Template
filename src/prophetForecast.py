import pandas as pd
from prophet import Prophet

import matplotlib.pyplot as plt



def prophetForecast(df):
    # Optional parser lambda to parse months
    # df = pd.read_csv('src/alameda.csv', parse_dates=['Date'], date_parser=lambda x:pd.to_datetime(x, format='%Y%m'))


    df1 = df[['Date', 'Value']]
    df1 = df1.rename(columns={'Date': 'ds', 'Value': 'y'})

    m = Prophet() # Defaults to linear growth, m = Prophet(growth='logistic')
    m.fit(df1)

    future = m.make_future_dataframe(periods=0, freq='MS') # Predict 6 months into future

    forecast = m.predict(future)
    # print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())


    # print("Forecasted Data: ")
    prediction = forecast[['ds', 'yhat']]
    # rolling_means = df1.y.rolling(window=6).mean()
    # rolling_stddev = rolling_means.rolling(window=6).std()
    # print("12 Month Prediction:")
    preds = prediction.tail(n=6)['yhat'].tolist()
    # print(preds)
    # print("Last 6 Month Real Values:")
    yvals = df1.tail(n=6)['y'].tolist()
    # print(yvals)

    diff = 0
    for i in range(6):
        # Sum of prediciton - actual
        diff += (preds[i] - yvals[i])
        # If negative: actual vals were higher, so less risk
        # If positive: actual vals were lower than predicted, so higher risk

    # fig1 = m.plot(forecast)

    # # Rolling mean
    plt.plot(df1.ds, df1.y.rolling(window=6).mean(), color="red")
    # # Rolling stddev
    # plt.plot(df1.ds, rolling_means.rolling(window=6).std(), label="rolling std (x10)", color="green")

    # plt.plot(forecast.ds[-(36+windowSize):], forecast.yhat[-(36+windowSize):].rolling(window=windowSize).mean(), color="purple")

    # fig2 = m.plot_components(forecast)

    # plt.show()

    return(diff)



if __name__ == '__main__':
    data = pd.read_csv('src/ca_precipitation.csv', parse_dates=['Date'], date_parser=lambda x:pd.to_datetime(x, format='%Y%m'))

    UniqueNames = data.Location.unique() #create unique list of names

    DataFrameDict = {elem : pd.DataFrame for elem in UniqueNames} #create a data frame dictionary to store your data frames
    CountyValues = {} # Dictionary to hold prediction values

    for key in DataFrameDict.keys():
        DataFrameDict[key] = data[:][data.Location == key]


    for key in DataFrameDict.keys():
        CountyValues[key] = prophetForecast(DataFrameDict[key])


    # print(DataFrameDict['Alameda County'])
    print(CountyValues)

