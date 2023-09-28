file=open("tekst.txt","r")
litery=[0]*26
licznik=0
linia=file.readline().strip()#odczytanie całej linii i wrzucenie pojedynczych słów na listę

for litera in linia:
     if litera!=' ':
          licznik+=1
          litery[(ord(litera)-65)]+=1

for i in range(26):
     lit=chr(i+65)
     procent=round((litery[i]/licznik)*100,2)
     print(lit,'-',litery[i],procent,'%')
     

