from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                    dtype={"fips": str})


output = {'Alameda County': -2.277383625457298, 'Alpine County': -3.5032597181025062, 'Amador County': -3.3389518753032226, 'Butte County': 0.8768487861326344, 'Calaveras County': -1.501829194305163, 'Colusa County': 0.06596588008868043, 'Contra Costa County': -1.8280713342750698, 'Del Norte County': 5.2836900263228985, 'El Dorado County': -4.929338159207077, 'Fresno County': -0.6495483391894972, 'Glenn County': 0.4778065144082495, 'Humboldt County': 7.007202491057963, 'Imperial County': 1.1701108915761034, 'Inyo County': 0.6276051725950618, 'Kern County': -0.008842199535437745, 'Kings County': -0.39289315040050066, 'Lake County': 1.26477916819875, 'Lassen County': -0.9649635791732565, 'Los Angeles County': -0.9400494734470235, 'Madera County': -1.6053742105156337, 'Marin County': -2.6818285724472304, 'Mariposa County': -2.493933714362387, 'Mendocino County': 1.2011075705668972, 'Merced County': 0.18641718174218624, 'Modoc County': 0.018744863503987075, 'Mono County': -1.6887848825493177, 'Monterey County': -0.0750626281220308, 'Napa County': -1.2805746177981483, 'Nevada County': -6.01656791087369, 'Orange County': 1.1253757235649013, 'Placer County': -6.145454239496529, 'Plumas County': -3.1251482992874324, 'Riverside County': 1.7408731871791834, 'Sacramento County': -1.963113345364766, 'San Benito County': -0.06796742235614239, 'San Bernardino County': 1.1841146273581624, 'San Diego County': 0.7849467143170068, 'San Francisco County': -3.6955494562943567, 'San Joaquin County': -1.4505864307880465, 'San Luis Obispo County': -0.7093609647146559, 'San Mateo County': -3.1296110982445535, 'Santa Barbara County': -0.969765569763569, 'Santa Clara County': -2.926875871693295, 'Santa Cruz County': -4.347397446890346, 'Shasta County': 2.1506909865198187, 'Sierra County': -6.21138138552381, 'Siskiyou County': 3.333466322629282, 'Solano County': -1.7291495386026545, 'Sonoma County': -0.8860808867481502, 'Stanislaus County': -0.9444790543774841, 'Sutter County': -0.6782693913355615, 'Tehama County': 0.8673454135551628, 'Trinity County': 5.8864918437740625, 'Tulare County': -2.1189547190035096, 'Tuolumne County': -1.545710317354824, 'Ventura County': -3.62555729858306, 'Yolo County': -1.7084896058819372, 'Yuba County': -0.9394145800710421}
countyFIPS = [
    ['06001',	'Alameda County',	'CA'],
    ['06003',	'Alpine County',	'CA'],
    ['06005',	'Amador County',	'CA'],
    ['06007',	'Butte County',	'CA'],
    ['06009',	'Calaveras County',	'CA'],
    ['06011',	'Colusa County',	'CA'],
    ['06013',	'Contra Costa County',	'CA'],
    ['06015',	'Del Norte County',	'CA'],
    ['06017',	'El Dorado County',	'CA'],
    ['06019',	'Fresno County',	'CA'],
    ['06021',	'Glenn County',	'CA'],
    ['06023',	'Humboldt County',	'CA'],
    ['06025',	'Imperial County',	'CA'],
    ['06027',	'Inyo County',	'CA'],
    ['06029',	'Kern County',	'CA'],
    ['06031',	'Kings County',	'CA'],
    ['06033',	'Lake County',	'CA'],
    ['06035',	'Lassen County',	'CA'],
    ['06037',	'Los Angeles County',	'CA'],
    ['06039',	'Madera County',	'CA'],
    ['06041',	'Marin County',	'CA'],
    ['06043',	'Mariposa County',	'CA'],
    ['06045',	'Mendocino County',	'CA'],
    ['06047',	'Merced County',	'CA'],
    ['06049',	'Modoc County',	'CA'],
    ['06051',	'Mono County',	'CA'],
    ['06053',	'Monterey County',	'CA'],
    ['06055',	'Napa County',	'CA'],
    ['06057',	'Nevada County',	'CA'],
    ['06059',	'Orange County',	'CA'],
    ['06061',	'Placer County',	'CA'],
    ['06063',	'Plumas County',	'CA'],
    ['06065',	'Riverside County',	'CA'],
    ['06067',	'Sacramento County',	'CA'],
    ['06069',	'San Benito County',	'CA'],
    ['06071',	'San Bernardino County',	'CA'],
    ['06073',	'San Diego County',	'CA'],
    ['06075',	'San Francisco County',	'CA'],
    ['06077',	'San Joaquin County',	'CA'],
    ['06079',	'San Luis Obispo County',	'CA'],
    ['06081',	'San Mateo County',	'CA'],
    ['06083',	'Santa Barbara County',	'CA'],
    ['06085',	'Santa Clara County',	'CA'],
    ['06087',	'Santa Cruz County',	'CA'],
    ['06089',	'Shasta County',	'CA'],
    ['06091',	'Sierra County',	'CA'],
    ['06093',	'Siskiyou County',	'CA'],
    ['06095',	'Solano County',	'CA'],
    ['06097',	'Sonoma County',	'CA'],
    ['06099',	'Stanislaus County',	'CA'],
    ['06101',	'Sutter County',	'CA'],
    ['06103',	'Tehama County',	'CA'],
    ['06105',	'Trinity County',	'CA'],
    ['06107',	'Tulare County',	'CA'],
    ['06109',	'Tuolumne County',	'CA'],
    ['06111',	'Ventura County',	'CA'],
    ['06113',	'Yolo County',	'CA'],
    ['06115',	'Yuba County',	'CA']
]

df1 = pd.DataFrame(output.items(), columns=['County', 'Score'])
# print(df)
df2 = pd.DataFrame(countyFIPS, columns=['FIPS', 'County', 'State'])
# print(df2)
df = pd.merge(df1, df2, on="County", how="inner")
# print(df)


import plotly.express as px

fig = px.choropleth(df, geojson=counties, locations='FIPS', color='Score',
                           color_continuous_scale="ylorrd",
                           range_color=(-10, 10),
                           scope="usa",
                           labels={'Score':'Predicted - Actual Precipitation in Last 6 Months'}
                          )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(fitbounds='locations', visible=False)
fig.show()