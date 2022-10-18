import csv
 
# opening the CSV file
with open('Asia Prod 1.csv', mode ='r') as file:   
        
       # reading the CSV file
       csvFile = csv.DictReader(file)
 
       # displaying the contents of the CSV file
       for lines in csvFile:
            print(lines)