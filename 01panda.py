import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print(pd.__version__)


#importing csv file to pandas


#import pandas as pd

#df = pd.read_csv('sample-1.csv', sep="\t",encoding="utf-16")
                 
#\\Tip: use to_string() to print the entire DataFrame.other wise it will print first 5 rows
#print(df)

