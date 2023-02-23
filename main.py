import csv
import random
from textblob import TextBlob


# Open the CSV file
with open('trumptweets.csv', encoding="utf8") as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
   # Loop through the rows in the CSV file
    row_count = 0
    for row in reader:
        if random.random() < 0.01:
            blob = TextBlob(row[2])
            sentiment_score = blob.sentiment.polarity
            if sentiment_score > 0.5:      
                print("Row number", row_count, "Sentiment score:", sentiment_score , "Noun_phrases", blob.noun_phrases, row[2])
        row_count += 1
    print(row_count)
    





