file=open('dane_geny.txt','r')

licznik=0
lista=[0]*500 #zerowanie listy 500 elementowej
for x in file:
    x=x.strip()
    dl=len(x)
    lista[dl]+=1#zliczamy długośći gatunków

for i in range(1,500):
    if lista[i]!=0:
        licznik+=1
        
print(max(lista))
print(licznik)
