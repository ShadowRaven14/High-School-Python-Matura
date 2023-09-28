file=open('liczby.txt','r')
suma=0
ilosc=0

for x in file:
    x=x.strip()
    a1=x
    a2=x[::-1]
    suma=int(a1)+int(a2)
    napis=str(suma)
    if napis==napis[::-1]:
        ilosc+=1
print(ilosc)
