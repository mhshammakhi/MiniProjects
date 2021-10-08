
from PyQt5.QtWidgets import QApplication, QWidget ,QTabWidget ,QGridLayout ,QLabel ,QLineEdit ,QGroupBox ,QPushButton ,\
    QComboBox ,QCheckBox ,QTableWidget ,QTableWidgetItem ,QPlainTextEdit
from PyQt5 import QtCore

class TotalGui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.brandsName=[]
        year_list=range(1350,1398,1)
        self.year_shamsi=['-']+list(map(lambda x: str(x) , year_list))
        self.year_miladi=['-']+list(map(lambda x: str(x+621) , year_list))
        self.search_list=[]
        self.data_test=[]

    def createGui(self):
        self.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.grid=QGridLayout(self)
        self.tab_buysell=QTabWidget()
        self.grid.addWidget(self.tab_buysell,0,0,1,4)
        self.widget_sell=QWidget()
        self.widget_buy=QWidget()
        self.tab_buysell.addTab(self.widget_buy,'خرید')
        self.tab_buysell.addTab(self.widget_sell,'فروش')
        self.groupDatabase=QGroupBox("برروزرسانی دیتابیس")
        self.gridBuy=QGridLayout(self.widget_buy)
        self.gridSell=QGridLayout(self.widget_sell)
        self.grid.addWidget(self.groupDatabase,0,4,1,1)
        self.gridDatabase=QGridLayout(self.groupDatabase)

        i=0
        self.label_brand=QLabel("برند:")
        self.gridBuy.addWidget(self.label_brand,i,0,1,1)
        
        self.combo_brand=QComboBox()
        self.gridBuy.addWidget(self.combo_brand,i,1,1,2)
        self.combo_brand.addItems([' ']+self.brandsName)

        self.label_model=QLabel("مدل:")
        self.gridBuy.addWidget(self.label_model,i,4,1,1)

        self.le_model=QLineEdit()
        self.gridBuy.addWidget(self.le_model,i,5,1,2)

        self.pb_search=QPushButton("جستحو")
        self.gridBuy.addWidget(self.pb_search,i,7,1,1)

        i+=1
        self.label_depreciation=QLabel("کارکرد")
        self.gridBuy.addWidget(self.label_depreciation,i,0,1,1)

        self.label_from_depreciation=QLabel("از:")
        self.gridBuy.addWidget(self.label_from_depreciation,i,1,1,1)
        self.le_from_depreciation=QLineEdit()
        self.gridBuy.addWidget(self.le_from_depreciation,i,2,1,2)
        
        self.label_to_depreciation=QLabel("تا:")
        self.gridBuy.addWidget(self.label_to_depreciation,i,4,1,1)
        self.le_to_depreciation=QLineEdit()
        self.gridBuy.addWidget(self.le_to_depreciation,i,5,1,2)

        i+=1
        self.label_year=QLabel("سال تولید")
        self.gridBuy.addWidget(self.label_year,i,0,1,1)

        self.label_from_year=QLabel("از:")
        self.gridBuy.addWidget(self.label_from_year,i,1,1,1)

        self.combo_year_from=QComboBox()
        self.gridBuy.addWidget(self.combo_year_from,i,2,1,1)
        
        self.combo_year_from.addItems(self.year_shamsi)

        self.year_unit_checkbox=QCheckBox('میلادی')
        self.gridBuy.addWidget(self.year_unit_checkbox,i,3,1,1)

        self.label_to_year=QLabel("تا:")
        self.gridBuy.addWidget(self.label_to_year,i,4,1,1)
        self.combo_year_to=QComboBox()
        self.combo_year_to.addItems(self.year_shamsi)
        self.gridBuy.addWidget(self.combo_year_to,i,5,1,1)
        
        self.year_unit_checkbox2=QCheckBox('میلادی')
        self.gridBuy.addWidget(self.year_unit_checkbox2,i,6,1,1)

        i+=1
        self.label_price=QLabel("قیمت")
        self.gridBuy.addWidget(self.label_price,i,0,1,1)

        self.label_from_price=QLabel("از:")
        self.gridBuy.addWidget(self.label_from_price,i,1,1,1)
        self.le_from_price=QLineEdit()
        self.gridBuy.addWidget(self.le_from_price,i,2,1,2)

        self.label_to_price=QLabel("تا:")
        self.gridBuy.addWidget(self.label_to_price,i,4,1,1)
        self.le_to_price=QLineEdit()
        self.gridBuy.addWidget(self.le_to_price,i,5,1,2)
        #------------------------------------------------------------------------#
        i=0
        self.label_brand_sell=QLabel("برند")
        self.gridSell.addWidget(self.label_brand_sell,i,0,1,1)
        
        self.combo_brand_sell=QComboBox()
        self.gridSell.addWidget(self.combo_brand_sell,i,1)
        self.combo_brand_sell.addItems([' ']+self.brandsName)

        self.label_model_sell=QLabel("مدل")
        self.gridSell.addWidget(self.label_model_sell,i,2)

        self.le_model_sell=QLineEdit()
        self.gridSell.addWidget(self.le_model_sell,i,3)

        self.label_depreciation_sell=QLabel("کارکرد")
        self.gridSell.addWidget(self.label_depreciation_sell,i,4,1,1)
        self.le_depreciation_sell=QLineEdit()
        self.gridSell.addWidget(self.le_depreciation_sell,i,5,1,2)
        
        i+=1
        self.label_year_sell=QLabel("سال تولید")
        self.gridSell.addWidget(self.label_year_sell,i,0,1,1)

        self.combo_year_sell=QComboBox()
        self.gridSell.addWidget(self.combo_year_sell,i,1,1,1)
        
        self.combo_year_sell.addItems(self.year_shamsi)

        self.year_unit_checkbox_sell=QCheckBox('میلادی')
        self.gridSell.addWidget(self.year_unit_checkbox_sell,i,2,1,1)

        self.pb_estimation=QPushButton("تخمین")
        self.gridSell.addWidget(self.pb_estimation,i,3,1,2)

        self.label_estimated_value=QLabel('')
        self.gridSell.addWidget(self.label_estimated_value,i,5,1,2)
        #------------------------------------------------------------------------#
        self.pb_start=QPushButton("شروع")
        self.gridDatabase.addWidget(self.pb_start,0,0)

        self.label_ndata=QLabel('')
        self.gridDatabase.addWidget(self.label_ndata,1,0)

        #------------------------------------------------------------------------#
        self.year_unit_checkbox.toggled.connect(self.shamsiMiladi)
        self.year_unit_checkbox2.toggled.connect(self.shamsiMiladi2)
        self.year_unit_checkbox_sell.toggled.connect(self.shamsiMiladi3)
        
    def shamsiMiladi(self):
        cf_index=self.combo_year_from.currentIndex()
        ct_index=self.combo_year_to.currentIndex()
        if(self.year_unit_checkbox.isChecked()):
            self.year_unit_checkbox2.setChecked(True)
            self.combo_year_from.clear()
            self.combo_year_to.clear()
            self.combo_year_from.addItems(self.year_miladi)
            self.combo_year_to.addItems(self.year_miladi)
        else:
            self.year_unit_checkbox2.setChecked(False)
            self.combo_year_from.clear()
            self.combo_year_to.clear()
            self.combo_year_from.addItems(self.year_shamsi)
            self.combo_year_to.addItems(self.year_shamsi)
        self.combo_year_from.setCurrentIndex(cf_index)
        self.combo_year_to.setCurrentIndex(ct_index)
    
    def shamsiMiladi2(self):
        cf_index=self.combo_year_from.currentIndex()
        ct_index=self.combo_year_to.currentIndex()
        if(self.year_unit_checkbox2.isChecked()):
            self.year_unit_checkbox.setChecked(True)
            self.combo_year_from.clear()
            self.combo_year_to.clear()
            self.combo_year_from.addItems(self.year_miladi)
            self.combo_year_to.addItems(self.year_miladi)
        else:
            self.year_unit_checkbox.setChecked(False)
            self.combo_year_from.clear()
            self.combo_year_to.clear()
            self.combo_year_from.addItems(self.year_shamsi)
            self.combo_year_to.addItems(self.year_shamsi)
        self.combo_year_from.setCurrentIndex(cf_index)
        self.combo_year_to.setCurrentIndex(ct_index)
    
    def shamsiMiladi3(self):
        c_index=self.combo_year_sell.currentIndex()
        if(self.year_unit_checkbox_sell.isChecked()):
            self.combo_year_sell.clear()
            self.combo_year_sell.addItems(self.year_miladi)
        else:
            self.combo_year_sell.clear()
            self.combo_year_sell.addItems(self.year_shamsi)
        self.combo_year_sell.setCurrentIndex(c_index)

    def readyDataToSearch(self):
        year_from=self.combo_year_from.currentText()
        if(len(year_from)==4):
            if(self.year_unit_checkbox.isChecked()):
                year_from=str(int(year_from)-621)
        year_to=self.combo_year_to.currentText()

        if(len(year_to)==4):
            if(self.year_unit_checkbox.isChecked()):
                year_to=str(int(year_to)-621)
        
        self.search_list=[self.combo_brand.currentText(),self.le_model.text(),\
                year_from,year_to,\
                self.le_from_depreciation.text(),self.le_to_depreciation.text(),\
                self.le_from_price.text(),self.le_to_price.text()]
    def readyToEstimation(self):
        if((self.combo_brand_sell.currentIndex() ==0) | (len(self.le_depreciation_sell.text())==0) |\
         (self.combo_year_sell.currentIndex()==0)):
            flagEstimation=False
        else:
            flagEstimation=True
        if(flagEstimation):
            try:
                year=int(self.combo_year_sell.currentText())
                if(year>1900):
                   year-=621 
                self.data_test=[self.combo_brand_sell.currentText(),self.le_model_sell.text(),\
                int(self.le_depreciation_sell.text()),year]
            except:
                flagEstimation=False
        return(flagEstimation)

class ResultGui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.grid=QGridLayout(self)
        self.searchTable=QTableWidget(self)
        self.searchTable.setColumnCount(4)
        self.searchTable.setHorizontalHeaderItem(0,QTableWidgetItem('برند و مدل'))
        self.searchTable.setHorizontalHeaderItem(1,QTableWidgetItem('سال تولید'))
        self.searchTable.setHorizontalHeaderItem(2,QTableWidgetItem('کارکرد'))
        self.searchTable.setHorizontalHeaderItem(3,QTableWidgetItem('قیمت (تومان)'))
        
        self.grid.addWidget(self.searchTable,0,0,5,5)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    
    def createTable(self,results):
        num_row=len(results)
        self.searchTable.setRowCount(num_row)
        for i in range(num_row):
            self.searchTable.setItem(i, 0, QTableWidgetItem('%s'%(results[i][0])))
            self.searchTable.setItem(i, 1, QTableWidgetItem('%i'%(results[i][1])))
            self.searchTable.setItem(i, 2, QTableWidgetItem('%i'%(results[i][2])))
            self.searchTable.setItem(i, 3, QTableWidgetItem('%i'%(results[i][3])))

class LogGui(QPlainTextEdit):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    def showing(self):
        self.clear()
        self.show()
        self.ShowText('Update DataBase ..... \nPlease Wait ...\n')
    def ShowText(self,text):
        self.appendPlainText(text)
