import pandas as pd
 
# to read csv file named "samplee"
a = pd.read_csv('C:\\Users\\rem31\\bootcamp\\ZZ-Homework\\python-api-challenge\\output_data\\city2.csv')

#C:\Users\rem31\bootcamp\ZZ-Homework\python-api-challenge\output_data


 
# to save as html file
# named as "Table"
a.to_html("Table.htm")
 
# assign it to a
# variable (string)
html_file = a.to_html()