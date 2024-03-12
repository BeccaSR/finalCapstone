#--------IMPORT PACKAGES--------

import pandas as pd
import numpy as np
import spacy
from textblob import TextBlob

# load spaCy model
nlp = spacy.load('en_core_web_sm')

#--------PREPROCESS DATA--------

# read csv file containing product reviews
df = pd.read_csv('amazon_product_reviews.csv')

reviews_data = df['reviews.text']
reviews_data.dropna(inplace=True, axis=0)
print(f'''
Null Values: {reviews_data.isnull().sum()}
Number of reviews: {reviews_data.count()}
Sample data:
{reviews_data[0:5]} 
''')

def preprocess(text):
    
    doc = nlp(str(text).strip())
    processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

    return ' '.join(processed)

#--------SENTIMENT ANALYSIS--------

def sentiment_calculation(text):
    
    processed = preprocess(text)
    
    doc = TextBlob(processed)

    polarity = doc.sentiment.polarity

    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment

print('Testing sentiment')
print(f'''
The review: {reviews_data[0]}
Sentiment: {sentiment_calculation(reviews_data[0])}
''')

print(f'''
The review: {reviews_data[483]}
Sentiment: {sentiment_calculation(reviews_data[483])}
''')

print(f'''
The review: {reviews_data[12805]}
Sentiment: {sentiment_calculation(reviews_data[12805])}
''')

print(f'''
The review: {reviews_data[33071]}
Sentiment: {sentiment_calculation(reviews_data[33071])}
''')

# while loop for user to enter number of review they wish to check sentiment of

positive = 0
negative = 0
netural = 0
count = 0

'''for i in reviews_data:
    if sentiment_calculation(i) == 'Positive':
        positive += 1
    elif sentiment_calculation(i) == 'Negative':
        negative += 1
        print(count)
    else:
        netural +=1
    count += 1'''

print(f'Pos:{positive}, Neg:{negative}, Neut:{netural}')

"""for i in range(0,reviews_data.count()):
    text = reviews_data[i]
    result = sentiment_calculation(text)
    if sentiment_calculation(i) == 'Positive':
        continue
    elif sentiment_calculation(i) == 'Negative':
        print(i)
        break
    else:
        continue
    """

