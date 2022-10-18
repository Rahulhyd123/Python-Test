import csv

for data in range(3):
    data = {'Source IP' : 11.11, 'Count' : 4, 'Events per Second' : 6}
print(data)

with open('NA Preview.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    
    # importing the module
import pandas as pd
  
# read specific columns of csv file using Pandas
df = pd.read_csv("Combined.csv", usecols = ['Source IP'])
print(df)

csv_list=['NA Preview.csv']

df_master=pd.read_csv('Combined.csv')

for csv_file in csv_list:
    df=pd.read_csv(csv_file)
    df.to_csv('Combined.csv',mode='a')