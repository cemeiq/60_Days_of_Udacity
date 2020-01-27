# -*- coding: utf-8 -*-
import requests
import pandas as pd
import numpy as np
import nltk
import string
import json
import string
import re
import spacy
import csv

nlp = spacy.load("en_core_web_sm")
filename="/home/iqra/Documents/testing-data.csv"
data_frame = pd.read_csv(filename , encoding='latin1',engine='c') 


ngram_list = []
word_start_list = []
word_end_list = []
word_cui = []

ngram_df = pd.DataFrame(columns=['ngram','start','end','cui'])

def preprocess(text):
    clean_data = []
    for x in (text[:][0]): #this is Df_pd for Df_np (text[:])
        new_text = re.sub('<.*?>', '', x)   # remove HTML tags
        new_text = re.sub(r'\d+','',new_text)# remove numbers   
        if new_text != '':
            clean_data.append(new_text)
    return clean_data

ascii_chars = set(string.printable)  # speeds things up
def remove_non_ascii_prinatble_from_list(list_of_words):
    return [word for word in list_of_words 
            if all(char in ascii_chars for char in word)]

for index,row in data_frame.iterrows():
	
	ngram_list=[]
	word_start_list=[]
	word_end_list=[]
	word_cui=[]
	text = row['abstract']+row['Article name']+"."
	text = nlp(text)
	sentences = list(text.sents)
	for i in sentences:
		
		#regex = re.compile('[^a-zA-Z]')
		
		s=i.text
		s = s.replace('"', '')
		s = s.replace("'", '')
		s = s.replace("[", '')
		s = s.replace("]", '')
		s = s.replace("{", '')
		s = s.replace("}", '')
		s = s.replace("/", '')
		s = s.replace("?", '')
		s = s.replace("!", '')
		s = s.replace(":", '')
		s = s.replace(";", '')
		s = s.replace(",", '')
		s = s.replace("@", '')
		s = s.replace("-", '')
		s = s.replace("_", '')
		s = s.replace("+", '')
		s = s.replace("*", '')
		s = s.replace("&", '')
		s = s.replace("<", '')
		s = s.replace(">", '')
		s = s.replace("%", '')
		s = s.replace("^", '')
		s = s.replace("#", '')
		s = s.replace("=", '')
		
		new_text = re.sub(r'[^\w\s]', '', s)
		
		new_string = ''.join([i for i in new_text if not i.isdigit()])
		#print(new_string)	
		json_data = requests.get('http://0.0.0.0:5000/'+new_string+"END")
	

		if json_data.status_code != 200:
					print(i);
				
		for entity in json_data.json():
				if entity['start'] in word_start_list and entity['end'] in word_end_list:
											continue
				else:
					ngram_list.append(entity['ngram'])
					#print(ngram_list)	
					word_start_list.append(entity['start'])
					word_end_list.append(entity['end'])
					word_cui.append(entity['cui'])
	
	combined_list = [ngram_list,word_start_list,word_end_list,word_cui]
	with open("/home/iqra/Desktop/output2.csv", "a") as fp:
	    	wr = csv.writer(fp, dialect='excel')
	    	wr.writerow(combined_list)

	
