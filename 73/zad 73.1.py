tekst=[]
licznik=0
file=open("tekst.txt","r")
tekst=file.readline().split()#odczytanie całej linii i wrzucenie pojedynczych słów na listę
print(tekst)
for slowo in tekst:
    if len(slowo)>1:
        for i in range(len(slowo)-1):
            if slowo[i]==slowo[i+1]:
                licznik+=1
                break #jesli w słowie są dwie pary podwójnych liter to liczymy jako jedno słowo
print(licznik)
