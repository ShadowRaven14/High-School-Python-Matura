def trojkat(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    return False


file=open("trojki.txt","r")
lista=[]
licznik=0
ciag=[]

for x in file:
    x=x.strip()
    lista.append(x.split())

for i in range(1000):
    if trojkat(int(lista[i][0]),int(lista[i][1]),int(lista[i][2])):
        licznik+=1
        ciag.append(1)
    else:
        ciag.append(0)
dl=1
najdl=0
for i in range(999):
    if ciag[i]==ciag[i+1]==1:
        dl+=1
    else:
        if dl>najdl:
            najdl=dl
        dl=1
    
print(licznik)
print(najdl)

