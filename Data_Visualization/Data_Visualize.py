
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px

class Data_Visualization:
    def __init__(self, data):
        self.data = data
        
        
    def Income_Month(self):
        gr_month= self.data.groupby("Month").sum()["TotalCost"]
        
        
    def TotalCost(self):
        months = range(1,13)
        plt.bar(months, gr_month, align='center')
        plt.xticks(months)
        plt.xlabel("Months")
        plt.ylabel("TotalCost")
    
    def VIP_customer(self):
        n= int(input("Nhập vào số lượng khách hàng VIP muốn xem: "))
        quan_stock = self.data.groupby("CustomerID").count()["InvoiceNo"]
        quan_stock= quan_stock.sort_values()
        quan_stock_top= quan_stock.nlargest(n)
        quan_stock_top.plot.bar()
        plt.title("Top khách hàng tiêu biểu")
        plt.ylabel("Số lần mua")
        plt.show()


    def bestsales_month(self):
        self.data['Year'].value_counts().plot(kind='pie', title="Sự phân bố dữ liệu giữa các năm")
        plt.pause(0.05)
        data_2010= self.data[self.data["Year"]==2010]
        data_2011= self.data[self.data["Year"]==2011]
        months = range(1,13)

        while (True):
            choice = int(input("Nhập vào năm bạn muốn xem tháng có doanh số cao nhất:\n1.2010\n2.2011\n3.Cả 2 năm\n4.Thoát\n"))
            if choice == 1:
                chart_style= int(input("Biểu đồ: \n1.Đường\n2.Cột\n"))
                if chart_style == 1:
                    gr_month = self.data.groupby('Month')['TotalCost'].sum().reset_index()
                    fig = px.line(gr_month, x ='Month', y ='TotalCost', template='plotly_dark',title="Tháng có doanh thu cao nhất")
                    fig.show()
                elif chart_style ==2:
                    gr_month= data_2010.groupby("Month").sum()["TotalCost"]
                    plt.bar(12, gr_month, align='center')
                    plt.xticks(months)
                    plt.xlabel("Months")
                    plt.ylabel("TotalCost")  
                    plt.title("Tháng có doanh thu cao nhất")     
                    plt.pause(0.05)
            elif choice == 2:
                chart_style= int(input("Biểu đồ: \n1.Đường\n2.Cột\n"))
                if chart_style == 1:
                    gr_month = self.data.groupby('Month')['TotalCost'].sum().reset_index()
                    fig = px.line(gr_month, x ='Month', y ='TotalCost', template='plotly_dark', title="Tháng có doanh thu cao nhất")
                    fig.show()
                elif chart_style ==2:
                    gr_month= data_2011.groupby("Month").sum()["TotalCost"]
                    plt.bar(months, gr_month, align='center')
                    plt.xticks(months)
                    plt.xlabel("Months")
                    plt.ylabel("TotalCost")  
                    plt.title("Tháng có doanh thu cao nhất")     
                    plt.pause(0.05)
            elif choice == 3:
                chart_style= int(input("Biểu đồ: \n1.Đường\n2.Cột\n"))
                if chart_style == 1:
                    gr_month = self.data.groupby('Month')['TotalCost'].sum().reset_index()
                    fig = px.line(gr_month, x ='Month', y ='TotalCost', template='plotly_dark', title="Tháng có doanh thu cao nhất")
                    fig.show()
                elif chart_style ==2:
                    gr_month= self.data.groupby("Month").sum()["TotalCost"]
                    plt.bar(months, gr_month, align='center')
                    plt.xticks(months)
                    plt.xlabel("Months")
                    plt.ylabel("TotalCost")
                    plt.title("Tháng có doanh thu cao nhất")    
                    plt.pause(0.05)
            else:
                break

    def bestsales_country(self):
        gr_country = self.data.groupby("Country").sum()["TotalCost"].sort_values(ascending= False).reset_index()
        fig=px.bar(gr_country, x='Country', y='TotalCost', width=900, title="Doanh số theo Country")
        fig.show() 


    def best_time(self):
        gr_hour = self.data.groupby("Hour").count()["TotalCost"]
        hour = [hour for hour, totalcost in gr_hour.items()]
        plt.plot(hour, gr_hour)
        plt.grid()
        plt.xticks(hour, size=8)
        plt.xlabel("Time")
        plt.ylabel("TotalCost")
        plt.title("Số lượng đơn hàng theo khung giờ")


    def combo_product(self):
        n = int(input("Nhập vào top combo muốn xem: "))
        data_dup = self.data[self.data["InvoiceNo"].duplicated(keep= False)]
        gr_product = lambda product: ','.join(product) 
        data_dup["All_Products"]= data_dup.groupby("InvoiceNo")["StockCode"].transform(gr_product)
        data_combo= data_dup[["InvoiceNo","All_Products"]].drop_duplicates()
        data_combo["All_Products"].value_counts()
        plt.rcParams['figure.figsize'] = (12, 10)
        a = data_combo["All_Products"].value_counts().head(n)
        sns.barplot(x = a.values, y = a.index, palette = 'inferno')
        plt.title('Top combo sản phẩm ', fontsize = 20)
        plt.ylabel('Names of Combo Product',fontsize=18)
        plt.xlabel
        plt.show()


    def bestsales_product(self):
        all_products_pri =  self.data.groupby("StockCode").mean()["UnitPrice"]
        all_products= self.data.groupby("StockCode").sum()['Quantity']
        product_ls = [StockCode for StockCode, Quantity in all_products.items()]
        quan_ls = [int(Quantity) for StockCode, Quantity in all_products.items()]
        price_ls = [UnitPrice for StockCode, UnitPrice in all_products_pri.items()]
        top_pro= all_products.sort_values()[3640:]
        pro_ls =  [StockCode for StockCode, Quantity in top_pro.items()]
        da = self.data.groupby(self.data["StockCode"]).mean()["UnitPrice"]
        da= pd.DataFrame(da)
        da= da.reset_index()
        avg_price=[]
        for i in pro_ls:
            arr = da[da["StockCode"] == str(i)]
            arr= np.array(arr)
            avg_price.append(arr[0][1])
        x= pro_ls
        y1= top_pro
        y2= avg_price
        fig, ax1 = plt.subplots()
        ax2= ax1.twinx()
        ax1.bar(x, y1, color = "g")
        ax2.plot(x, y2, 'b-')

        ax1.set_xticklabels(pro_ls, rotation=90, size=8)
        ax1.set_xlabel("Products")
        ax1.set_ylabel("Quatity")
        ax2.set_ylabel("Price Each")
        ax1.set_title("Sản phẩm bán chạy và giá thành sản phẩm")
        plt.show()


    def Menu_Visua(self):
        while(True):
            choice = int(input('-------------------------THÔNG TIN MUỐN XEM-------------------------------\n1. Khách hàng VIP\n2. Tháng có doanh số cao nhất\n3. Country có doanh số cao nhất\n4. Sản phẩm nào bán chạy nhất và tại sao?\n5. Các combo sản phẩm thường được mua cùng nhau\n6. Doanh nghiệp nên quảng cáo vào khung giờ nào?\n7. Thoát\n'))
            if choice==1:
                self.VIP_customer()
            elif choice ==2:
                self.bestsales_month()
            elif choice==3:
                self.bestsales_country()
            elif choice==4:
                self.bestsales_product
            elif choice==5:
                self.combo_product()
            elif choice==6:
                self.best_time()
            else:
                break

        
    def RFM_model(self):
        fig = px.scatter(RFM_data,x = "Recency", y = "Frequency",color = "RFM_Loyality_level")
        fig.show()

        fig = px.scatter(RFM_data,x = "Monetary", y = "Frequency",color = "RFM_Loyality_level")
        fig.show()

        fig = px.scatter(RFM_data,x = "Monetary", y = "Recency",color = "RFM_Loyality_level")
        fig.show()


    def KMean_model(self):
        fig = px.scatter(RFM_data,x = 'Recency',y = 'Frequency', color = 'Cluster')
        fig.show()

        fig = px.scatter(RFM_data,x = 'Monetary',y = 'Frequency', color = 'Cluster')
        fig.show()

        fig = px.scatter(RFM_data,x = 'Monetary',y = 'Recency', color = 'Cluster')
        fig.show()
