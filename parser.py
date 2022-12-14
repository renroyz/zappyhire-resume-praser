# -*- coding: utf-8 -*-
"""parser.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J1ciVypGZknecx7CMFs1jhAMJRU8ZT6l
"""

#installing pypdf2
pip install pypdf2

#importing pypdf2
import PyPDF2

#opening pdf file
pdfFileObj = open('/resume.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

text=''
for i in range(0,pdfReader.numPages):
    # creating a page object
    pageObj = pdfReader.getPage(i)
    # extracting text from page
    text=text+pageObj.extractText()
print(text)

#finding phone number
ph = re.compile(r"\d\d\d\d\d\d\d\d\d\d\d\d")

a=re.findall(ph,text)
if len(a)==0:
  ph = re.compile(r"\d\d\d\d\d\d\d\d\d\d")
  a=re.findall(ph,text)
print(a)

#installing spacy
!pip install spacy

!python -m spacy download en_core_web_lg

import spacy
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_lg")

# Process whole documents
doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

#import spacy
import spacy
nlp = spacy.load("en_core_web_lg")
tokens = nlp(text)
#finding name
PERSON=[t for t in tokens.ents if t.label_ == 'PERSON']
print('Name: ',PERSON[0])
#finding phone number
phone=[t for t in tokens.ents if t.label_ == 'CARDINAL']
print('Phone number: ',phone[0])
#finding email
import re
E = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
email=re.findall(E, text)
print('Email: ',email)
#finding skills
skills=[t for t in tokens.ents if t.label_ == 'ORG']
print('Skills: ',skills)
# import csv
# with open('/skills.csv', 'r') as f:
#     reader = csv.reader(f)
#     sk=re.findall(reader,skills)
