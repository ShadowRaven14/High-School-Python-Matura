def pierwsza(a):
    d=2
    while d*d<=a:
        if a%d==0:
            return False
        d+=1
    return True


file=open("trojki.txt","r")
lista=[]

for x in file:
    x=x.strip()
    lista.append(x.split())

for i in range(1000):
    a=int(lista[i][0])
    b=int(lista[i][1])
    c=int(lista[i][2])
    if (pierwsza(a) and pierwsza(b)) and c==a*b:
        print (lista[i])

