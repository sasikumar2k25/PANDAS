 
#importing csv file to pandas


import pandas as pd

df = pd.read_csv('sample-1.csv', sep="\t",encoding="utf-16")
                 
#\\Tip: use to_string() to print the entire DataFrame.other wise it will print first 5 rows
print(df)

