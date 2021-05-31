import pandas as pd

class data_preprocessing:
    def __init__(self, data):
        self.data= data
        
    def True_Data(self):
        self.data = self.data[pd.notnull(self.data['CustomerID'])]
        self.data = self.data.query("Quantity > 0")
        return self.data
        
    def Add_Colunm(self):
        self.data['Date']=[item[0] for item in self.data['InvoiceDate'].str.split()]
        self.data['Time']=[item[1] for item in self.data['InvoiceDate'].str.split()]
        self.data['Hour']=[item[0] for item in self.data['Time'].str.split(':')]
        self.data['Month']=[item[0] for item in self.data['Date'].str.split('/')]
        self.data['Year']=[item[1] for item in self.data['Date'].str.split('/')]
        self.data['TotalCost']=self.data['Quantity']*self.data['UnitPrice']
        return self.data
    
    def Data(self):
        return pd.DataFrame(self.data)
        
