import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
import time
def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return False

    dbcur.close()
    return True

def updateDatabase(choosen_car,last_page,cursor,table_name):    
    # Data Extraction
    n=0
    page_n=1
    flag_finish=False

    while(not flag_finish):
        r = requests.get('https://bama.ir/car/%s?page=%i'%(choosen_car,page_n))
        soup_agahi=BeautifulSoup(r.text,'html.parser')
        agahi_obj=soup_agahi.findAll('div',attrs={'class':"listdata"})
        for each_obj in agahi_obj:
            price_description='None'
            name_part=each_obj.find('h2',attrs={'itemprop':'name'}).text
            name_description=re.sub(r'[\s|،]*\n\s*',',',name_part.strip())
            year=int(name_description.split(',')[0])
            if(year>1900):
                year-=621
            name_description=(' '.join(name_description.split(',')[1:]))[0:50].strip()

            depreciation_part=each_obj.find('p',attrs={'class':'price hidden-xs'}).text
            depreciation=re.sub(r'\s*\n\s*',',',depreciation_part.strip())
            if(re.search(r'\d[\d|,]*',depreciation_part)!=None):
                depreciation=re.findall(r'\d[\d|,]*',depreciation_part)[0]
                depreciation=re.sub(r',','',depreciation)
                depreciation=int(depreciation)
            elif(re.search(r'صفر',depreciation_part)!=None):
                depreciation=0
            else:
                continue  
            cost_part=each_obj.find('p',attrs={'class':'cost'})
            
            if(cost_part.get('content')=='0'):
                continue
            try:
                tmp=cost_part.find('span')
            
                if (tmp['content']=='0'):
                    continue
                else:
                    price_description=re.findall(r'\d[\d|,]*',cost_part.text.strip())[0]
                    price_description=re.sub(r',','',price_description)
                    price_description=int(price_description)
                    
            except:
                continue
            cursor.execute('SELECT * FROM %s WHERE Name=\'%s\' AND Year=%i AND Depreciation=%i AND Price=%i;'%(table_name,name_description,year,depreciation,price_description))
            search_result=cursor.fetchall()
            if len(search_result)==0:
                cursor.execute('INSERT INTO %s VALUES (\'%s\',\'%i\',\'%i\',\'%i\');'%(table_name,name_description,year,depreciation,price_description))
            else:
                continue
            n+=1
        if page_n==last_page:
            flag_finish=True
            break
        page_n+=1
    print(n)

def main(logWidget,table_name,cnx):
    #Car Type Extraction
    car_brands=dict()
    car_brands_en=[]
    r = requests.get('https://bama.ir/car')

    soup=BeautifulSoup(r.text,'html.parser')
    brand_obj=soup.findAll('select',attrs={'class':'filter-custom-select','id':'selectedTopBrand'})
    brands=brand_obj[0]
    for option in brands.find_all('option'):
        tmp=option['value'].split(',')
        if(len(tmp)<2):
            continue
        car_brands[option.text]=tmp[1].strip()
        car_brands_en.append(tmp[1].strip())
    #Car Type Extraction Completed
    # Data Base Modify
    cursor = cnx.cursor()
    # Update Data Base Top 20 Page
    updateDatabase('',20,cursor,table_name)
    logWidget.ShowText('update '+'20 Page'+' done!')
    print('update '+'20 Page'+' done!')
    # Update Data Base (Brand Base)
    for brand in car_brands_en:
        
        updateDatabase(brand,5,cursor,table_name)
        print('update '+brand+' done!')
        logWidget.ShowText('update '+brand+' done!')
    cursor.execute('SELECT COUNT(*) FROM %s;'%(table_name))
    n_row=cursor.fetchall()[0][0]
    cnx.commit()
    return(n_row)


def searchDatabase(mylist,cnx,table_name):    
    # Data Base Modify
    cursor = cnx.cursor()
    request_context='SELECT * FROM %s WHERE'%(table_name)
    try:
        if(mylist[0]!=' '):
            request_context+=' Name LIKE \'%%%s%%\''%(mylist[0])
        if(mylist[1]!=' '):
            request_context+=' AND Name LIKE \'%%%s%%\''%(mylist[1])            
        if(len(mylist[2])==4):
            request_context+=' AND Year>=%i'%(int(mylist[2]))
        if(len(mylist[3])==4):
            request_context+=' AND Year<=%i'%(int(mylist[3]))
        if(len(mylist[4])>0):
            request_context+=' AND Depreciation>=%i'%(int(mylist[4]))
        if(len(mylist[5])>0):
            request_context+=' AND Depreciation<=%i'%(int(mylist[5]))
        if(len(mylist[6])>0):
            request_context+=' AND Price>=%i'%(int(mylist[6]))
        if(len(mylist[7])>0):
            request_context+=' AND Price<=%i'%(int(mylist[7]))
        cursor.execute(request_context+';')
        search_result=cursor.fetchall()
        
    except:
        search_result=[]
    cnx.commit()
    return(search_result)