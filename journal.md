Feb. 2 - I have added a large enough dataset containing important drought information on the United States from February 2016 until February 2022. This will serve as the primary dataset unless another one is found that I deem to be better, and I will do my initial tests on the csv file in /src. 


Feb. 9 - Now looking for bigger and more decipherable dataset to fit the model to. My model will need to fit the data and ideally output a classification for what severity of drought the data point is in, ranging through 5 categories from 'severe drought' to 'no drought'. I am considering logistic regression and/or stochastic gradient descent to fit the model, but I will need to play with this and start running some tests.


Feb. 19 - I have found a nice dataset here: https://www.ncdc.noaa.gov/cag/county/mapping/4/pcp/201902/1/value and will be changing the model to be one for an unsupervised classification problem. This dataset has monthly precipitation data for all counties of California, where I will be focusing my model on first, from 1895 to January of 2022. I will need to decide how to split up the data into training, testing, validation, and potentially hold-out. I will also be doing tests to see how the data looks and if there are any additional patterns to be observed. 


Feb. 28 - I found a machine learning Python package that helps with KMeans clustering. I have added a test Python file in /src that will test out this functionality before applying it to my dataset and observing the patterns. 


March 15 - Decided to try alternative seasonal forecasting method: Facebook's Prophet: https://facebook.github.io/prophet/. Have added python file testing this out and will analyze results. Also found this resource: https://stackoverflow.com/questions/19790790/splitting-dataframe-into-multiple-dataframes to split into many dataframes based on column value, which I need to use to separate the different dataframes for each California county. Need to think of a nice way to display the data on maybe a CA map.


March 31 - Have completed model, and have added code to run the model automatically for all counties in CA and generate a score, which is the predicted - actual precipitation values for the last 6 months. This score is used in the newest code I wrote to generate a choropleth map of California, color-coding which counties have the highest likelihood of drought. All the coding is done, and I just have to finish the abstract, and start work on the final paper and video. 



Resources for final paper:


https://www.google.com/search?q=what+forecasting+model+does+prophet+use&oq=what+forecasting+model+does+prophet+use&aqs=chrome..69i57.5323j0j7&sourceid=chrome&ie=UTF-8 - what model Prophet uses

https://www.drought.gov/what-is-drought/monitoring-drought#:~:text=Drought%20indicators%20describe%20drought%20conditions,%2C%20soil%20moisture%2C%20and%20snowpack. - Factors to drought



python3 -u "/Users/user/Downloads/ML-Climate-Final-Project-Template/src/prophetForecast.py"
