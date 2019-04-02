import tkinter as tk 
import random 
import os, glob, time
import time, datetime
import PyPDF3
import sys
import argparse
import glob, random
import LibraryMini as lib
from tkinter import * 
if not sys.warnoptions:
	import warnings
	warnings.simplefilter("ignore")


parser = argparse.ArgumentParser()
parser.add_argument("gui")
parser2 = argparse.ArgumentParser()
parser2.add_argument("cli")
args = parser.parse_args()
args2 = args.gui


if args2 == "gui":

	root = tk.Tk() ## Creating the root window
	root.title("Forensic program") ## Setting the title 
	root.geometry("1100x700+150+300")

	## Functions of the program ##
	 ## Block contains the encrypt function and the get function from the entry box
	def encrypt():
		while True:
			try:
				key = [5]
				with open(encryptValue,"r") as klass:
					redklass = klass.read()
				
				hold_en = ""
				pointer = 0
				for my_char in range(len(redklass)):
					hold_en += chr(ord(redklass[my_char]) + key[pointer])
					pointer += 1
					if pointer >= len(key):
						pointer = 0
				klass.close()
				f = open(encryptValue, "w")
				f.write(hold_en)
				f.close()
				return hold_en
				
				break

			except Exception as e:
				print("Something went wrong! Please try again!")
				break
	def getEncryptValue():
		global encryptValue
		encryptValue = encryptBox.get()

	## Block contains the decrypt function and the get function from the entry box
	def decrypt():
		key = [5]
		with open(decryptValue,"r") as klass:
			redklass = klass.read()
	 
		hold_en = ""
		pointer = 0
		for my_char in range(len(redklass)):
			hold_en += chr(ord(redklass[my_char]) - key[pointer])
			pointer +=1
			if pointer >= len(key):
				pointer = 0
		klass.close()
	 
		f = open(decryptValue, "w")
		f.write(hold_en)
		f.close()
	 
		return hold_en 
	def getDecryptValue():
		global decryptValue
		decryptValue = decryptBox.get()

	## Block contains the find files function and the get function from the entry box
	def findFilesFunction():
		namn = findValue
		allafiler = []
		for root, dirs, files in os.walk(namn):
			allafiler += files
		print(allafiler) 
	def getFindValue():
		global findValue
		findValue = findBox.get()

	## Block contains the find by type function and the two get functions from the entry boxes.
	def findByTypeFunction():
		flista = []
		for file in os.listdir(FindByTypePath):
			if file.endswith(FindByTypeExt):
				flista.append(os.path.join(file))
		print(flista)    
	def getFindByTypeValue():
		global FindByTypePath
		FindByTypePath = findByTypeBox.get()
	def getFindByTypeValueExtFunction():
		global FindByTypeExt
		FindByTypeExt = findByTypeBox2.get()

	## Block contains the search for specific word function and gets information from entries. 
	def spec():
		flista = []
		for file in os.listdir(pathFromSearch):
			if file.endswith(extensionFromSearch):
				flista.append(os.path.join(file))

		for i in flista:
			p = (pathFromSearch + i) #Kombinerar för att föra in i with open. 
			
			
			with open(p, "r") as f:
				for line in f:
					if wordFromSearch in line:
						print(i)
					else:
						pass 
	def getPathFromSearch():
		global pathFromSearch
		pathFromSearch = pathBox.get() 
	def getExtensionFromSearch():
		global extensionFromSearch 
		extensionFromSearch = pathExtensionBox.get()
	def getWordfromSearch():
		global wordFromSearch
		wordFromSearch = searchWordBox.get()

	## Block contains the modified function and gets information from entry box
	def showLatestModified():
		mod_list = [] #Lista för att lägga in fil-stat

		#dinp = int(input("Ange datum för senaste modifikation enligt följande: xxxx,x,x (ÅÅRR,M,D) för en mer specifik sökning lägg till timme, minut och sekund: "))
		datum = datetime.datetime(sendYear,sendMonth,sendDay).timestamp() #År, månad, dag, timme, minut
		
			
		print("Mapp = ", modifiedPath) #Printa ut vilken mapp man är i.
		
		filer = os.listdir(modifiedPath) #Listar alla filer i mappen.
		#print(filer)
		for i in filer: #För varje fil i mappen
			#print(i)
			fn = modifiedPath + i #fn får hela sökvägen för att kunna använda i stat()
			
			p = os.stat(fn).st_mtime
			c = [fn, p]
			#print(c)
			
			if c[1] > datum:
				st = os.stat(fn) #Kör os.stat() på alla filer
				lastmod_date = time.localtime(st[8])
				#print(lastmod_date)
				nytuple = (lastmod_date, fn) #Lägger in all info och sökväg i en tuple.
				mod_list.append(nytuple) #Stoppar in det i mod_list.
		mod_list.sort() #Sorterar listan
		mod_list.reverse()

		for m in mod_list:
			mapp, namn = os.path.split(m[1]) # Splittar så mapp kommmer i en lista och filnamn i en annan.
			
			m_datum = time.strftime("%m/%d/%y %H:%M:%S", m[0]) #Gör om till rätt format.
			print("%-40s %s" % (namn, m_datum))
	def sendDates():
		global sendYear 
		sendYear = yearBox.get()
		sendYear = int(sendYear)
		global sendMonth
		sendMonth = monthBox.get()
		sendMonth = int(sendMonth)
		global sendDay 
		sendDay = dayBox.get()
		sendDay = int(sendDay)
	def sendPathModified():
		global modifiedPath
		modifiedPath = modifiedBox.get()

	def pdf_search():
		redpdf = PyPDF3.PdfFileReader(open(pdfPath, 'rb'))
	 
		count = 0
	 
		for sida in range(0,redpdf.numPages):
			temptext = redpdf.getPage(sida)
			text = temptext.extractText()
			start = 0
			kontroll = 0
		   
			while kontroll != -1:
				kontroll = text[start:].find(pdfWord)
				if kontroll != -1:
					start+= kontroll + len(pdfWord)
					count = count +1
				else:
					break
			   
		print(pdfWord, "finns", count, "gånger i dokumentet")

	def getPathOne():
		global pathOne 
		pathOne = compareBoxOne.get()

	def getPathTwo():
		global pathSecond 
		pathSecond = compareBoxTwo.get()


	def FileAnalyze():
		p1 = pathOne
		p2 = pathSecond

		fil1 = set(open(p1).read().split())
		fil2 = set(open(p2).read().split())

		same = fil1.intersection(fil2)

		diff = fil1.difference(fil2)

		diff2 = (fil2.difference(fil1))

		print("Filern innehåller båda:", "\n", same)

		print("Fil 1: ", p1, "innehåller utöver ovanstående:", "\n", diff)
		print("Fil 2: ", p2, "innehåller utöver ovanstående:", "\n", diff2)


	def getPdfPath():
		global pdfPath
		pdfPath = findPdfBox.get()
	def getPdfWord():
		global pdfWord
		pdfWord = searchPdfBox.get()



	## GUI ## 

	######################ENCRYPT#################################

	## Encrypt file button 
	encryptIt = tk.Button(root,width=20, text="Encrypt", command=encrypt)
	encryptIt.grid(row=2, column=0)

	## encrypt box 
	encryptBox = Entry(root, width=20, bg="light gray")
	encryptBox.grid(row=2, column=1)

	## Send EncryptValue 

	sendEncrypt = tk.Button(root, text="Send Path", command=getEncryptValue)
	sendEncrypt.grid(row=2, column=2)
	#########################END ENCRYPT#####################################


	################################DECRYPT##################################

	decryptIt = tk.Button(root,width=20, text="Decrypt", command=decrypt)
	decryptIt.grid(row=3, column=0)

	decryptBox = Entry(root, width=20, bg="light gray")
	decryptBox.grid(row=3, column=1)

	## Send DecryptValue 
	sendDecrypt = tk.Button(root, text="Send Path", command=getDecryptValue)
	sendDecrypt.grid(row=3, column=2)
	###################################END DECRYPT###############################


	##################################FIND FILES IN SYSTEM#######################

	## Find file button and defines grid 
	find_file = tk.Button(root, width=20,text="Find Files", command=findFilesFunction)
	find_file.grid(row=4, column=0)

	## input box for the findFileFunction
	findBox = Entry(root, width=20, bg="light gray")
	findBox.grid(row=4, column=1)

	## Send Value from find files
	sendFileValue = tk.Button(root, text="Send Path", command=getFindValue)
	sendFileValue.grid(row=4, column=2)

	###################################END FIND FILES IN SYSTEM##################


	###################################FIND FILE BY TYPE ##################
	## Find file by type.
	find_bytype = tk.Button(root,width=20, text="Find File by type", command=findByTypeFunction) #, command=find_bytype_window)
	find_bytype.grid(row=5, column=0)

	## inputBox for path
	findByTypeBox = Entry(root, width=20, bg="light gray")
	findByTypeBox.grid(row=5, column=1)
	## Input for extension
	findByTypeBox2 = Entry(root, width=20, bg="light gray")
	findByTypeBox2.grid(row=5, column=3)

	sendFileByTypeValue = tk.Button(root, text="Send Path", command=getFindByTypeValue)
	sendFileByTypeValue.grid(row=5, column=2)

	sendFileByTypeValueExt = tk.Button(root, text="Send Extension", command=getFindByTypeValueExtFunction)
	sendFileByTypeValueExt.grid(row=5, column=4)
	###################################FIND FILE BY TYPE END##################


	########################## SEARCH WORD IN SPECIFIC FILE ################################
	search_word = tk.Button(root, width=20,text="Search word in files", command=spec) 
	search_word.grid(row=6, column=0)

	## inputBox for searchWordbox function
	pathBox = Entry(root, width=20, bg="light grey")
	pathBox.grid(row=6, column=1)

	sendPathButton = tk.Button(root, text="Send Path", command=getPathFromSearch)
	sendPathButton.grid(row=6, column=2)

	pathExtensionBox = Entry(root, width=20, bg="light gray")
	pathExtensionBox.grid(row=6, column=3)

	sendExtensionButton = tk.Button(root, text="Send Extension", command=getExtensionFromSearch)
	sendExtensionButton.grid(row=6, column=4)

	searchWordBox = Entry(root, width=20, bg="light gray")
	searchWordBox.grid(row=6, column=5)

	sendWordButton = tk.Button(root, text="Send word", command=getWordfromSearch)
	sendWordButton.grid(row=6, column=6)
	############################SEARCH WORD IN SPECIFIC FILE END##############################


	############################SHOW LATEST MODIFIED FILES#################################### 

	## Find file by modified
	find_modified = tk.Button(root, width=20,text="Find latest modified files", command=showLatestModified)
	find_modified.grid(row=8, column=0)

	## modifiedBox
	modifiedBox = Entry(root, width=20, bg="light gray") ## Skriv in pathen här. 
	modifiedBox.grid(row=8, column=1)

	## Send pathen 
	skickaPath = tk.Button(root, text="Send Path", command=sendPathModified)
	skickaPath.grid(row=8, column=2)
	yearBox = Entry(root, width=10, bg="light gray")
	yearBox.grid(row=8, column=3)

	monthBox = Entry(root, width=10, bg="light gray")
	monthBox.grid(row=8, column=4)

	dayBox = Entry(root, width=10, bg="light gray")
	dayBox.grid(row=8,  column=5)

	sendDateValues = tk.Button(root, text="Send Dates", command=sendDates)
	sendDateValues.grid(row=8, column=6)

	###########################SHOW LATEST MODIFIED FILES END#################################



	############################SEARCH PDF##############################

	## Find file button and defines grid 
	pdfButton = tk.Button(root, width=20,text="Search word in pdf", command=pdf_search)
	pdfButton.grid(row=7, column=0)

	findPdfBox = Entry(root, width=20, bg="light gray")
	findPdfBox.grid(row=7, column=1)

	sendFileValue = tk.Button(root, text="Send Path", command=getPdfPath)
	sendFileValue.grid(row=7, column=2)

	## Search word and send it 
	searchPdfBox = Entry(root, width=20, bg="light gray")
	searchPdfBox.grid(row=7, column=3)

	sendFileValue = tk.Button(root, width=13, text="Send word", command=getPdfWord)
	sendFileValue.grid(row=7, column=4)



	##########################SEARCH PDF END###############################

	###########################ANALYZE##############################

	find_bytype = tk.Button(root,width=20, text="File analysys", command=FileAnalyze) #, command=find_bytype_window)
	find_bytype.grid(row=9, column=0)

	## inputBox for path
	compareBoxOne = Entry(root, width=20, bg="light gray")
	compareBoxOne.grid(row=9, column=1)

	sendFileByTypeValue = tk.Button(root, text="Send Path", command=getPathOne)
	sendFileByTypeValue.grid(row=9, column=2)
	## Input for extension
	compareBoxTwo = Entry(root, width=20, bg="light gray")
	compareBoxTwo.grid(row=9, column=3)

	sendFileByTypeValueExt = tk.Button(root, text="Send path to compare", command=getPathTwo)
	sendFileByTypeValueExt.grid(row=9, column=4)

	###############################ANALYZE END##############################å



	root.resizable(False, False)
	root.configure(background="black")

	root.mainloop()


else:
	

	def meny():
		print("MENY")
		print("1) Hitta alla filer.")
		print("2) Filer av en viss typ.")
		print("3) Info i viss typ av fil.")
		print("4) Pdf.")
		print("5) Senast modiefierade filer.")
		print("6) Kryptera/Dekryptera.")
		print("7) Filanalys.")
		print("q) Exit.")

	def main():
		choice = "0"
		while choice != "q":
			meny()
			choice = input("Ange val:")
			if choice == "1":
				lib.search()
			elif choice == "2":
				lib.typ()
			elif choice == "3":
				lib.spec()
			elif choice == "4":
				#lib.main3()
				print("PDF")
			elif choice == "5":
				lib.modi()
			elif choice == "6":
				lib.main2()
			elif choice == "7":
				lib.FileAnalyze()
			   
main()

print("Programmet avslutas")



