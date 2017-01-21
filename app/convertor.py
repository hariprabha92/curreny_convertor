import json
import requests
def convertfun(amount,params):

   # params={}
    #params={'base':base, 'symbols':symbols}
    api = requests.get('http://api.fixer.io/latest', params=params)
    json_format = api.json()
    symbol=params['symbols']
 #   print(symbol)
  #  print(amount)
    rate =float(json_format['rates'][symbol])
  #  print (rate)
    c = amount*rate
    print(c)

    return c

#c=conversion(1,'USD','SGD')
#print c
    
