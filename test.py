import pandas as pd

my_data = pd.read_excel('Raw_Data.xlsx')

def max_price(mydata,types):
    gr_my_data = my_data.groupby(['BRAND HOUSE','BRANDNAME'])["PRICE"].agg(types)
    return gr_my_data


print(max_price(my_data,'max'))
print(max_price(my_data,'min'))
 