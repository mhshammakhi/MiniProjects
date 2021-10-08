import mysql.connector
import numpy as np
from sklearn import tree

def extractDataTrain(mylist,cursor,table_name):    
    # Data Base Modify
    request_context='SELECT * FROM %s WHERE'%(table_name)
    request_context+=' Name LIKE \'%%%s%%\''%(mylist[0])
    if(mylist[1]!=' '):
        request_context+=' AND Name LIKE \'%%%s%%\''%(mylist[1])            
    cursor.execute(request_context+';')
    search_result=cursor.fetchall()
    return(search_result)

def estimPrice(mylist,cnx,table_name):
    cursor = cnx.cursor()
    results=extractDataTrain(mylist[0:2],cursor,table_name)
    if(len(results)<3):
        return('lowData',0)
    x_Train_data=list(map(lambda x: list(x[1:3]) , results))
    y_Train_data=list(map(lambda x: x[3] , results))
    
    clf=tree.DecisionTreeRegressor(max_depth=4)
    clf=clf.fit(x_Train_data,y_Train_data)
    new_data=[[int(mylist[2]),int(mylist[3])]]
    answer=clf.predict(new_data)
    return('ok',int(answer[0]))

    
