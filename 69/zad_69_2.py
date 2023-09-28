file=open('dane_geny.txt','r')
lista=[]
licznik=0

for x in file:
    x=x.strip()
    i=0
    while i<len(x)-4:
        nowy=''
        if x[i]=='A' and x[i+1]=='A':
            indeks=i
            i+=2
            while (x[i]!='B' or x[i+1]!='B') and i<len(x)-4:
                i+=1
            if x[i]=='B' and x[i+1]=='B':
                koniec=i+2
                nowy=x[indeks:koniec]
                print(nowy)
                lista.append(nowy)
        i+=1
        
#print(lista)
for s in lista:
    if 'BCDDC' in s:
        licznik+=1

print(licznik)
