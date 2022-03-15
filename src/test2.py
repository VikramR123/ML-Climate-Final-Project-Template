import csv
import numpy as np
import matplotlib.pyplot as plt

from tslearn.clustering import TimeSeriesKMeans
from tslearn.generators import random_walks

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing as HWES
#from statsmodels.nonparametric.smoothers_lowess import lowess


x = []
y = []
 
with open('src/test.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        #print(row[3])
        x.append(int(row[2])) # Date as int
        y.append(float(row[3])) # Inches of precipitation that month


x1 = [1, 2, 3]
y1 = [5, 6, 7]




# Time Series KMeans Clustering from tslearn

# X = random_walks(n_ts=50, sz=32, d=1)

# # print(X)
# km = TimeSeriesKMeans(n_clusters=3, metric="euclidean", max_iter=5, random_state=0).fit(X)

# print(km.cluster_centers_.shape)


# RANDOM TESTING W RAIN DATASET
#x2 = x.reshape(-1, 1)
x2 = np.reshape(x, (-1, 1))
km = TimeSeriesKMeans(n_clusters=3, metric="softdtw", max_iter=5, max_iter_barycenter=5, metric_params={"gamma": .5}, random_state=0).fit(x2) # metric = "euclidean" does not work
print(km.cluster_centers_.shape)
print(km.labels_.shape)

#print(km.labels_)

# Plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
# Precipitation data
# plt.plot(x, y, color="red")

# Rolling mean
d = {'date': x, 'rain': y}
df = pd.DataFrame(data=d)
# print(df.rain)
plt.plot(df.date, df.rain, color="red")
plt.plot(df.date, df.rain.rolling(window=12).mean(), color="black")

plt.plot(df.date, df.rain.rolling(window=60).mean(), color="blue")



# Exponential Smoothing model for times series forecast/regression
model = HWES(df.rain, seasonal_periods=12, trend='add', seasonal='add')
fitted = model.fit(optimized=True, use_brute=True)

#print out the training summary
print(fitted.summary())

#create an out of sample forcast for the next 12 steps beyond the final data point in the training data set
sales_forecast = fitted.forecast(steps=12)
new_dates = list(range(202201, 202212))
new_dates.append(202301)

plt.plot(new_dates, sales_forecast, color="orange")

# Labels from model
#plt.plot(x, km.labels_, color="blue")


plt.show()


# km_dba = TimeSeriesKMeans(n_clusters=3, metric="dtw", max_iter=5, max_iter_barycenter=5, random_state=0).fit(X)

# print(km_dba.cluster_centers_.shape)

# km_sdtw = TimeSeriesKMeans(n_clusters=3, metric="softdtw", max_iter=5, max_iter_barycenter=5, metric_params={"gamma": .5}, random_state=0).fit(X)

# print(km_sdtw.cluster_centers_.shape)

# X_bis = to_time_series_dataset([[1, 2, 3, 4], [1, 2, 3], [2, 5, 6, 7, 8, 9]])
# km = TimeSeriesKMeans(n_clusters=2, max_iter=5, metric="dtw", random_state=0).fit(X_bis)

# print(km.cluster_centers_.shape)
