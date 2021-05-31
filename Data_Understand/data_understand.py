class data_understand:
    
    def __init__(self, data):
        self.data = data
    def basic_info(self):
        while(True):
            choice= int(input('*'*15+"Basic_Info"+ '*'*15+"\n1.The first five rows\n2.List colunms\n3.Sum of NaN values\n4.Showing Basics Statistics\n5.Displaying Data Types\n6.Exis\n"))
            if choice == 1:
                print(self.data.head())
            elif choice == 2:
                print(list(self.data.columns))
            elif choice ==3:
                print(self.data.isna().sum())   
            elif choice ==4:
                print(self.data.describe())   
            elif choice ==5:
                print(self.data.info()) 
            else:
                break

    def count_customer_country(self):
        country_data = self.data[['Country','CustomerID']].drop_duplicates()
        return country_data.groupby(['Country']).agg({'CustomerID' : 'count'}).sort_values('CustomerID',ascending = False).reset_index().rename(columns = {'CustomerID':'CustomerID Count'})
    
    def count_country(self):
        print("Country \t Values_Counts\n")
        return self.data['Country'].value_counts()
