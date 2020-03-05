from textblob import TextBlob
import json

companies = []

with open('data.json') as jsonfile:
    companies = json.load(jsonfile)

for company in companies:
    blob = TextBlob(company['purpose'])
    company['sentiment'] = blob.sentiment.polarity

def bySentiment(c):
    return c['sentiment']

companies.sort(key=bySentiment)

topTen = companies[-10:]
bottomTen = companies[:10]

print("TOP TEN")
for c in topTen:
    print(c['name'], " -- ", c['sentiment'])

print("BOTTOM TEN")
for c in bottomTen:
    print(c['name'], " -- ", c['sentiment'])