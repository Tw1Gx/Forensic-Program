import glob, os, random
#import PyPDF2


def search():
	namn = input("Ange en path: ")
	allafiler = [] #Lista för alla filer
	for root, dirs, files in os.walk(namn): #För root, alla mappar och filer i sökkvägen.
		allafiler += files #Lägger till alla filer i listan.
	print(allafiler)


#search()

def typ():
	unikp = input("Ange en sökväg: ")
	end = input("Ange filtyp: ")
	flista = []
	for file in os.listdir(unikp): #För filer i sökvägen.
		if file.endswith(end): #Om filerna slutar med end
			flista.append(os.path.join(file)) #Lägger in filerna som slutar på end
	print(flista)
	return flista	

#typ()

def spec():
	# Blev lite rörigare än tänkt att kalla på funktion i funktionen i GUI därför finns hela typ() inskriven i denna.
	unikp = input("Ange en sökväg: ")
	end = input("Ange filtyp: ")
	s = input("Ange sökord: ")
	flista = []
	for file in os.listdir(unikp):
		if file.endswith(end):
			flista.append(os.path.join(file))

	for i in flista:
		p = (unikp + i) #Kombinerar för att föra in i with open. 
		
		
		with open(p, "r") as f: #Öppnar varje fil med hela sökvägen i read.
			for line in f: # För varje linje i filen
				if s in line: # Om sökordet finns i filen
					print(i) #Printa ut det filnamnet
				else:
					pass #Om sökordet inte finns, skippa den filen. 
#spec()

def FileAnalyze():
	p1 = input("Ange sökväg till fil 1: ") #Fil 1
	p2 = input("Ange sökväg till fil 2: ") #Fil 2

	fil1 = set(open(p1).read().split()) #Lägger innehåll i Fil 1 i set, genom att öppna i read och splitta vid " ".
	fil2 = set(open(p2).read().split())

	same = fil1.intersection(fil2) #Tar det som är detsamma i båda filerna. 

	diff = fil1.difference(fil2) #Det som Fil 1 har men inte Fil 2

	diff2 = fil2.difference(fil1) #Det som Fil 2 har men inte Fil 1

	print("Filern innehåller båda:", "\n", same)

	print("Fil 1: ", p1, "innehåller utöver ovanstående:", "\n", diff)
	print("Fil 2: ", p2, "innehåller utöver ovanstående:", "\n", diff2)



#FileAnalyze()

import os, time, datetime
def modi():
	mod_list = [] #Lista för att lägga in fil-stat
	y = int(input("Ange år(xxxx): "))
	m = int(input("Ange månad(x): " ))
	d = int(input("Ange dag(x): "))
	
	datum = datetime.datetime(y,m,d).timestamp() #År, månad, dag, timme, minut. Sekunder mellan datum användaren skriver in och January 1, 1970
	
		
	
	a = input("Ange sökväg: ") #Sökväg
	print("Mapp = ", a) #Printa ut vilken mapp man är i.
	
	filer = os.listdir(a) #Listar alla filer i mappen.
	#print(filer)
	for i in filer: #För varje fil i mappen
		#print(i)
		fn = a + i #fn får hela sökvägen för att kunna använda i stat()
		
		p = os.stat(fn).st_mtime
		c = [fn, p]
		#print(c)
		
		if c[1] > datum:
			st = os.stat(fn) #Kör os.stat() på alla filer
			lastmod_date = time.localtime(st[8]) #Tar ut endast tid från stat. 
			#print(lastmod_date)
			nytuple = (lastmod_date, fn) #Lägger in all info och sökväg i en tuple.
			mod_list.append(nytuple) #Stoppar in det i mod_list.
	mod_list.sort() #Sorterar listan
	mod_list.reverse() #Vänder på ordningen. 

	for m in mod_list:
		mapp, namn = os.path.split(m[1]) # Splittar så mapp kommmer i en lista och filnamn i en annan.
		
		m_datum = time.strftime("%m/%d/%y %H:%M:%S", m[0]) #Gör om till rätt format.
		print("%-40s %s" % (namn, m_datum))
#modi()

def main2():
    val = input("1 eller 2: ")
    file = input("Skriv in filen: ")

    key = [5]

    if val == "1":
        enc = encrypt(file, key)
        print(enc)

    elif val == "2":
        denc = decrypt(file, key)
        print(denc)

    else:
        main()

def encrypt(file, key):
    with open(file,"r") as klass:
        redklass = klass.read()

    temp_text = ""
    for my_char in range(len(redklass)):
        temp_text += chr(ord(redklass[my_char]) + key[pointer])
    klass.close()

    f = open(file, "w")
    f.write(temp_text)
    f.close()
    return temp_text

def decrypt(file, key):
    with open(file,"r") as klass:
        redklass = klass.read()

    temp_text = ""
    for my_char in range(len(redklass)):
        temp_text += chr(ord(redklass[my_char]) - key[pointer])
    klass.close()

    f = open(file, "w")
    f.write(temp_text)
    f.close()

    return temp_text

#main2()

def pdf_search(file, word):
    redpdf = PyPDF2.PdfFileReader(open(file, 'rb'))
    count = 0

    for sida in range(0,redpdf.numPages):
        temptext = redpdf.getPage(sida)
        text = temptext.extractText()
        start = 0
        kontroll = 0
        
        while kontroll != -1:
            kontroll = text[start:].find(word)
            if kontroll != -1:
                start+= kontroll + len(word)
                count = count +1
            else:
                break
            
    print(word, "finns", count, "gånger i dokumentet")

def main3():
    file = input("Vilken fil vill du söka i? ")
    word = input("Vilket ord ska kontrolleras? ")

    pdf_search(file, word)

#main3()