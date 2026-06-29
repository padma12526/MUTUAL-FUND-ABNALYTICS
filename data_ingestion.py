import pandas as pd
import os


files=os.listdir("data/raw")
for i in files:
    if i.endswith(".csv"):
        df=pd.read_csv(os.path.join("data/raw",i))
        print("="*60)
        print("File Name:",i)
        print("="*60)
        print(df.head())
        print("Shapes:",df.shape)
        print("Coloumns:",list(df.columns))
        print(df.dtypes)
        print("="*56)
        print("ANAMOLIES CHECK")
        print("="*56)
        print("MISSING VALUES:\n",df.isnull().sum())
        print("DUPLICATE VALUES:",df.duplicated().sum())
        print("COMPLETELY EMPTY ROWS:",df.isnull().all(axis=1).sum())
        
        
