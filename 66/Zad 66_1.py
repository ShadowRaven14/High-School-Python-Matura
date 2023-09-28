def suma_cyfr(a):
    suma=0
    while a>0:
        suma+=a%10
        a=a//10
    return suma


file=open("trojki.txt","r")
lista=[]

for x in file:
    x=x.strip()
    lista.append(x.split())

for i in range(1000):
    a=int(lista[i][0])
    b=int(lista[i][1])
    c=int(lista[i][2])
    if (suma_cyfr(a)+suma_cyfr(b))==c:
        print (lista[i])
