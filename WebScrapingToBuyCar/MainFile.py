#In The Name Of God
DataBase_Name='mh'
UserName='root'
Password='1234'
Table_Name='Total3'

from PyQt5.QtWidgets import QApplication
import mysql.connector

from GuiClasses import TotalGui , ResultGui , LogGui
from SiteManager import RequestManger
import DatabaseFunctions
import EstimationAlgorithms as EA

class connectManger():
    def __init__(self):
        self.gui=None
        self.guiResult=None
        self.guiLog=None
        self.request=None
        self.cnx=None
        self.database_name=self.table_name=''

    def checkAndConnect(self,database_name,table_name,user_name,password):
        self.database_name=database_name
        self.table_name=table_name
        self.cnx = mysql.connector.connect(user=user_name, password=password, host='127.0.0.1', database=self.database_name,charset='utf8')
        cursor = self.cnx.cursor()
        if DatabaseFunctions.checkTableExists(self.cnx,self.table_name):
            cursor.execute('CREATE TABLE %s (Name VARCHAR(50), Year INT(4),Depreciation INT(9), Price BIGINT(12)) \
            ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4;'%(self.table_name))
        cursor.execute('SELECT COUNT(*) FROM %s;'%(self.table_name))
        ndata=cursor.fetchall()[0][0]
        self.gui.label_ndata.setText('تعداد کل داده‌ها: %s'%(str(ndata)))
        self.cnx.commit()

    def refreshDatabase(self):
        self.guiLog.showing()
        ndata=DatabaseFunctions.main(self.guiLog,self.table_name,self.cnx)
        self.gui.label_ndata.setText('تعداد کل داده‌ها: %s'%(str(ndata)))
        self.cnx.commit()
        print('----------------Done! ----------------------')
    
    def searchStart(self):
        self.gui.readyDataToSearch()
        search_results=DatabaseFunctions.searchDatabase(self.gui.search_list,self.cnx,self.table_name)
        self.guiResult.createTable(search_results)
        myconnect.guiResult.show()
        self.cnx.commit()

    def estimation(self):
        flag_estimation=self.gui.readyToEstimation()
        if(flag_estimation):
            situ,estimate_value=EA.estimPrice(self.gui.data_test,self.cnx,self.table_name)
            if(situ=='ok'):
                self.gui.label_estimated_value.setText(str(estimate_value)+' تومان')
            else:
                self.gui.label_estimated_value.setText('تعداد داده برای تخمین کم است')
        self.cnx.commit()
        
myconnect=connectManger()

myRequests=RequestManger()
myconnect.request=myRequests

myRequests.checkBrands()

app = QApplication([])
myguiobj = TotalGui()
myguiobj.brandsName=myRequests.brands
myguiobj.createGui()

myconnect.gui=myguiobj
myconnect.checkAndConnect(DataBase_Name,Table_Name,UserName,Password)

myguires = ResultGui()
myconnect.guiResult=myguires

myguilog = LogGui()
myconnect.guiLog=myguilog

myguiobj.pb_start.clicked.connect(myconnect.refreshDatabase)
myguiobj.pb_search.clicked.connect(myconnect.searchStart)
myguiobj.pb_estimation.clicked.connect(myconnect.estimation)
myguiobj.show()
app.exec_()

