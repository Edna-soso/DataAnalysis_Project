import numpy as np
import pandas as pd
import files

class data_preprocessing:
    def __init__(self):
        super.__init__()
        
    def True_Data(self):
        data.isna().sum()
        self.data = data[pd.notnull(data['CustomerID'])]
        self.data = data.query("Quantity > 0")  
        
    def Add_Colunm(self):
         data['Date']=[item[0] for item in data['InvoiceDate'].str.split()]
         data['Time']=[item[1] for item in data['InvoiceDate'].str.split()]
         data['Hour']=[item[0] for item in data['Time'].str.split(':')]
         data['Month']=[item[0] for item in data['Date'].str.split('/')]
         data['TotalCost']=data['Quantity']*data['UnitPrice']
    
    def Dow_Data(self,data):
        data.to_csv('filename.csv') 
        files.download('filename.csv')
