import csv
import json

companies = []

def readTXT(filename):
    with open(filename) as txtfile:
        lines = txtfile.read().splitlines()
        nameList = []
        purposeList = []
        for line in lines:
            words = line.split(' ')
            if len(words):
                if words[0] == 'Name:':
                    nameList.append(" ".join(words[1:]))
                elif words[0] == 'Purpose:':
                    purposeList.append(" ".join(words[1:]))
        for (name, purpose) in zip(nameList, purposeList):
            companies.append({'name': name, 'purpose': purpose})

def readJSON(filename):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
    for company in data:
        companies.append(company)

def readCSV(filename, nameField, purposeField):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            companies.append({
                'name': row[nameField],
                'purpose': row[purposeField]
            })


readTXT(filename='companies/1.txt')
readTXT(filename='companies/2.txt')
readTXT(filename='companies/3.txt')
readTXT(filename='companies/4.txt')
readJSON(filename='companies/5.json')
readCSV(filename='companies/6.csv', nameField='name', purposeField='purpose')
readCSV(filename='companies/7.csv', nameField='Name', purposeField='Purpose')
readCSV(filename='companies/8.csv', nameField='Name', purposeField='Purpose')
readCSV(filename='companies/9.csv', nameField='Name', purposeField='Purpose')
readCSV(filename='companies/10.csv', nameField='name', purposeField='purpose')

with open('data.json', 'w') as outfile:
    json.dump(companies, outfile)
