def suma_cyfr(a):
    suma=0
    for i in range(len(a)):
        suma+=int(a[i])
    return suma


file=open("trojki.txt","r")
lista=[]

for x in file:
    x=x.strip()
    lista.append(x.split())

for i in range(1000):
    a=lista[i][0]
    b=lista[i][1]
    c=int(lista[i][2])
    if (suma_cyfr(a)+suma_cyfr(b))==c:
        print (lista[i])
