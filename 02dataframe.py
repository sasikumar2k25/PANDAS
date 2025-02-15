#creating a data frame in pandas01

import pandas as pd

data1 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
dataframe = pd.DataFrame(data1)

print(dataframe,  "\n")

#creating another data frame in pandas02

import pandas as pd  

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)  # Creating a DataFrame
print(df)


#my own creating data frame

collg_data = {'NAME':['sasikumar','gopi','irfhan','venkatsh','mukesh','hari','bhargavi','obulesh','gowtham'],
              "FROM":['narayanpuram','rajupalem','nellore','chevuru','kavali','kavali','nellore','badvel','vizag'],
              "ROLL.NO":[13,34,32,5,19,2,57,31,41],
              "percentage":[80,90,90,90,90,90,90,90,90]

              
              }
data_frnds = pd.DataFrame(collg_data)#\\it will print whole data which was given by us

#print("\n\n\n",data_frnds)


#\\indexing slicing in pandas with syntax and examples\\

#print(data_frnds.head(5)) #\\it means it prints first 5 numbers from top\\
#print(data_frnds.tail(3)) #\\it means it prints from last 3 numbers from bottom\\ 
#print(data_frnds.describe())#\\ once print you will understand the describe function concept\\
#print(data_frnds.shape) #\\shape function shows the number of rows and no colunms ,once you print you will get clarity on that\\
#print(data_frnds[0:8:2])#\\means here the syntax is "[start:stop:step]" it will start from o and ends with 8 by the step of difference 2\\
#print(data_frnds["NAME"])#\\ this syntax is usefull for execute only the colunms what the name we given\\
#print(data_frnds[['NAME','FROM']])#\\this also like above one but here to increase the columns we should must use the two closed brackets[[]]\\
#print(data_frnds[['NAME','FROM']][0:5:1] ) #\\here i used both -->column,start:stop:step syntax then it will execute like combination\\
#print(data_frnds.duplicated())#\\if a name & value repeated twice then it will show TRUE or else it will show FALSE\\
#print(data_frnds.drop_duplicates())#\\it will remove the duplicates for temporary time only not perminate for perminate we have another syntax\\ 
#print =(data_frnds.to_csv("C:\\Users\\batha\\OneDrive\\Microsoft Edge Drop Files\\Documents\\Desktop\\players.csv"))
#print(data_frnds.loc[1])#\\this .loc[] is used to select a row which you wanted to select\\to select more rows we have .loc[[1,2,3]] this syntax
#\\Tip: use to_string() to print the entire DataFrame.other wise it will print first 5 rows
#print(data_frnds.to_string())
#You can check your system's maximum rows with the pd.options.display.max_rows statement.
#print(pd.options.display.max_rows)
#Print information about the data .info():
#print(data_frnds.info())
#\\exporting dataframe in the form of csv file\\
#data_frnds.to_csv("C:\\Users\\batha\\OneDrive\\Microsoft Edge Drop Files\\Documents\\Desktop\\playerslist.csv",index=False)
#print("csv file has been saved")
