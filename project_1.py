import pandas as pd 

def load (file_name):
    if 'csv' in (file_name).lower():
        data = pd.read_csv(file_name)
    elif 'excel' in (file_name).lower():
        data = pd.read_excel
    elif 'json' in (file_name).lower():
        data = pd.read_json
    else:
        return print("Check the file name")   
    
    df=pd.DataFrame(data)
    return df
        

        
def data_info (df):
    print(df.info())
    
     
def calc (df , col_name):
    if col_name not in df:
        print('the column does not exist') 
    else:
        print (df[col_name].isna())
        print (df[col_name].isna().sum())
    return df[col_name].isna().sum()
       

        


df = load('shopping1_behavior.csv')
data_info(df)
calc(df , 'Item Purchased')
