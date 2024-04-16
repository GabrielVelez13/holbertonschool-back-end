#!/usr/bin/python3
import csv

# some data to be written to csv file
data = [['Name', 'Age'], ['Alex', 21], ['Bob', 22], ['Clarke', 23]]

# writing to csv file
with open('people.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    
    # writing the data
    csvwriter.writerows(data)