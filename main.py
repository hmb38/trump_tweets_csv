import csv
import random



# Open the CSV file
with open('trumptweets.csv', encoding="utf8") as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
   # Loop through the rows in the CSV file
    row_count = 0
    for row in reader:
        if random.random() < 0.001:
            print(row[2])
        row_count += 1
    print(row_count)
        
        # Access the data in each row
        # print(row)


