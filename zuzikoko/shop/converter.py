#import libraries to handle request to api
import requests
import json
import pprint

'''
# base currency or reference currency
base="CZK"

# required currency for plot
out_curr="EUR"

# exchange data from a date
start_date="2022-11-10"

# exchange data till a date
end_date="2022-11-10"

# api url for request 
url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(base,start_date,end_date,out_curr)
response = requests.get(url)

# retrive response in json format
data = response.json()
'''

#retrieved data here
data = {'motd': {'msg': 'If you or your company use this project or like what we doing, please consider backing us so we can continue maintaining and evolving this project.', 'url': 'https://exchangerate.host/#/donate'}, 'success': True, 'timeseries': True, 'base': 'CZK', 'start_date': '2022-11-10', 'end_date': '2022-11-10', 'rates': {'2022-11-10': {'EUR': 0.041184}}}
exchange_rate = list(data.items())[6][1]['2022-11-10']['EUR']
