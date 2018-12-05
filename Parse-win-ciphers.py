# import libraries 
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime 
import easygui
import sys
import os 
 

# Please Select Input file "Host_ciphers.text file "

Inputfile = easygui.fileopenbox(filetypes = ['Host_ciphers.txt'])
with open (Inputfile, 'r') as cipher_input:
	with open ('Host_ciphers_analyzed.csv', 'a') as csv_file:
		writer = csv.writer(csv_file,delimiter = ',') 
		for CipherSuite in cipher_input:
			CipherSuite = CipherSuite.strip()
			url = requests.get("https://ciphersuite.info/search/?",params={'q': CipherSuite})
			soup = BeautifulSoup(url.text, "html.parser")
			#Response Filter
			Link = soup.find_all('span',attrs={'class' : ['label label-fixed-width label-danger','label label-fixed-width label-recommended','label label-fixed-width label-success','label label-fixed-width label-warning']})[0]
			Response = Link.text.strip()
			#Score Mapping
			lis=[]
			out = ""
			if Response == 'Secure':
				Security = 'Secure'
				Score = '2'
			#print(Security,Score,CipherSuite)
			elif Response == 'Recommended':
			 	Security = 'Recommended'
			 	Score = '3'
			#print(Security,Score,CipherSuite)
			elif Response == 'Weak':
				Security = 'Weak'
				Score = '1'
			#print(Security,Score,CipherSuite)
			elif Response =='Insecure':
				Security = 'Insecure'
				Score = '0'
			#print(Security,Score,CipherSuite)
			else:
				Security = "N/A"
				Score = "N/A"

			lis.append(CipherSuite)
			lis.append(Security)
			lis.append(Score)
			out = ";".join(lis)
			writer.writerow([out,datetime.now()])
	csv_file.close()
cipher_input.close()
			




         
