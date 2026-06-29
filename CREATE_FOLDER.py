import os
folders=["data/raw","data/processed","notebooks","sql","dashboard","reports"]
for i in folders:
    os.makedirs(i,exist_ok=True)
    print(i,"=>CREATED")