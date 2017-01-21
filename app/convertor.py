import json
import requests
def convertfun(amount,params):
    api = requests.get('http://api.fixer.io/latest', params=params)
    json_format = api.json()
    symbol=params['symbols']
    rate =float(json_format['rates'][symbol])
    c = amount*rate
    return c
    
