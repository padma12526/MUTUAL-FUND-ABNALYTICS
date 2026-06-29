import pandas as pd
import requests
print("============FETCHING LIVE NAV DATA===============\n")
scheme_code="119551"
url=f"https://api.mfapi.in/mf/{scheme_code}"
        
response=requests.get(url)
        
print("Status Code:")
response.status_code

if response.status_code==200:      
        data=response.json()
        
        print("Fund Name:",data["meta"]["scheme_name"])
        
        nav_def=pd.DataFrame(data["data"])
        
        print("\nNAV DATA(TOP 5):")
        print("COLOUMNS:",nav_def.columns)
        print(nav_def.dtypes) 
        
        print("Missing Values",nav_def.isnull().sum())
        print("Duplicates:",nav_def.duplicated().sum())       
        
        print("\n=================SAVING FILES=================\n")
        output_path="data/processed/nav_data.csv"
        nav_def.to_csv(output_path,index=False)
        print("File saved at:",output_path)
else:
    print("Failed to fetch data.")
        