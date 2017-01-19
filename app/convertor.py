import json
import requests
def conversion(amount,base,symbols):

    params={}
    params={'base':base, 'symbols':symbols}
    api = requests.get('http://api.fixer.io/latest', params=params)
    json_format = api.json()
    rate =float(json_format['rates'][symbols])
    print (rate)
    converted_amount = amount * rate
    return converted_amount

#c=conversion(1,'USD','SGD')
#print c
    
