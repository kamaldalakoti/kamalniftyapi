from django.http import JsonResponse

from itertools import product
import json
import pandas as pd
# Create your views here.
import json
import requests
# we can pass prams for dates home(date1,date1 , mail=true or false)
# for mail add a if condition before for loop
list=[]
def home():
    date1 = '2022-01-04'
    date2 = '2022-01-29'
    response_API = requests.get('https://api.informedinvestorr.com/assignment/python/niftyList')
    response_API2 = requests.get(f'https://api.informedinvestorr.com/assignment/python/dailyPrices/?selected_date={date1}')
    response_API2_a = requests.get(f'https://api.informedinvestorr.com/assignment/python/dailyPrices/?selected_date={date2}')
    data = response_API.text
    data2 = response_API2
    data_list = response_API2
    data_list2 = response_API2_a
    # data2 = response_API2.text
    data2 = data_list.text
    data2b = data_list2.text
    data_nifty =  response_API.text
    # print(data_nifty)
    print(response_API.status_code)
    a = json.loads(data2)['data_list']
    b = json.loads(data2b)['data_list']
    nifty = json.loads(data_nifty)['fincode_list']
   
    for item in nifty:
        output_dict = [a for a in a if a['fincode'] == item]
        output_dict_b = [b for b in b if b['fincode'] == item]
       
        for element,element2 in product(output_dict, output_dict_b):
           
           
            # print(element)
            A_fincode = element['fincode' ]
            A_symbol = element['symbol' ]
            A_close = element['close' ]
            # print(A_fincode , A_close)
            B_close = element2['close' ]
            
            performance = abs(A_close - B_close)/((A_close+B_close)/2)*100
            performance = round(performance , 2)
                
            if A_close > B_close:
                performance = "-"+str(performance)+"%"  
            elif A_close < B_close:
                performance = str(performance)+"%"  
            # print(performance)
            dictF = { 'fincode' : A_fincode , 'symbol' : A_symbol , 'closing_start': A_close , 'closing_end' : B_close , 'performance' : performance } 
            # print(dictF) 
            json_object = json.dumps(dictF)
            list.append(dictF)
            f = open("demofile3.txt", "a")  
            f2 = open("demofile1.txt", "a")  
            f.write(str(dictF))              
            # f2.write(str(json_object))              
            f2.write(json_object)              
    
    add = json.dumps(list)
    f2 = open("jsonnifty.txt", "a")  
    f2.write(add)              
    # data = json.load(add)  
    # df = pd.DataFrame(data)   
    # df.to_excel('exported_json_data.xlsx')  
    with open('jsonnifty.txt') as json_file:
        data = json.load(json_file)  
        df = pd.DataFrame(data)   
        df.to_excel('exported_json_data.xlsx')  
    # print(list)
    # print(add)
               
home()
