file=open("tekst.txt","r")
litery=[0]*26
licznik=0
linia=file.readline().strip()#odczytanie całej linii i wrzucenie pojedynczych słów na listę

slownik = {
     "A": 0,
     "B": 0,
     "C": 0,
     "D": 0,
     "E": 0,
     "F": 0,
     "G": 0,
     "H": 0,
     "I": 0,
     "J": 0,
     "K": 0,
     "L": 0,
     "M": 0,
     "N": 0,
     "O": 0,
     "P": 0,
     "Q": 0,
     "R": 0,
     "S": 0,
     "T": 0,
     "U": 0,
     "V": 0,
     "W": 0,
     "X": 0,
     "Y": 0,
     "Z": 0,
     }

for litera in linia:
     if litera in slownik:
          slownik[litera]+=1
     if litera!=' ':
          licznik+=1

#licznik = sum(slownik.values())
for litery, ilosc in slownik.items():
     procent = round((ilosc/licznik)*100, 2)
     print(litery,":",ilosc,"(",procent,")","%")
