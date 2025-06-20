import numpy as np
import pandas as pd

dict1 = {
    "name": ["Shruti", "Abhishek", "Aditi", "Harsh"],
    "marks": [10, 7, 6, 1],
    "city": ['jabalpur', 'bhopal', 'mandla', 'kolkata']
}

df = pd.DataFrame(dict1)                                        #creates a dataframe. like a table
print(df)
df.to_csv('friends.csv')                                        #creates csv file in the folder

df.to_csv('friends.csv', index=False)                           #excludes the indexing

print(df.head(2))                                               #returns upper two rows
print(df.tail(2))                                               #returns lower two rows
print(df.describe())                                            #mathematical description of numerical columns in the data

shr = pd.read_csv('shruti.csv')                                 #to read a csv file in the folder
print(shr)

shr['Speed'][0] = 50                                            #to change the value in the df
print(shr)                                                      
shr.to_csv('shruti.csv')                                        #to update the csv file in the folder

shr.index = ['1st', '2nd', '3rd', '4th']                        #it is not necessary that indexes are numbers. they can be anything
print(shr)
