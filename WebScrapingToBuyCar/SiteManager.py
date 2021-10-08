#In The Name Of God

import mysql.connector
import requests
from bs4 import BeautifulSoup

class RequestManger():
    def __init__(self):
        self.urlsite='https://bama.ir/car'    

        self.car_brands=dict()
        self.brands=[]

        self.car_models=dict()
        self.models=[]
    #Car Type Extraction
    def checkBrands(self):
        
        r = requests.get(self.urlsite)
        soup=BeautifulSoup(r.text,'html.parser')
        brand_obj=soup.findAll('select',attrs={'class':'filter-custom-select','id':'selectedTopBrand'})
        brands=brand_obj[0]
        for option in brands.find_all('option'):
            tmp=option['value'].split(',')
            if(len(tmp)<2):
                continue
            self.car_brands[option.text]=tmp[1].strip()
            self.brands.append(option.text)
    
