def koncowka(a,b):
    dl1=len(a)
    dl2=len(b)
    i=0
    while a[dl1-1-i]==b[dl2-1-i] and i<dl1 and i<dl2:
        i+=1
    return(i)
        
lista=[]
zlicz=[]
licznik=0
file=open("napisy.txt","r")
for x in file:
    x=x.strip()
    lista.append(x.split())

for i in range(200):
    a=lista[i][0]
    b=lista[i][1]
    zlicz.append(koncowka(a,b))
maks=max(zlicz)
print(maks)

for i in range(200):
    if zlicz[i]==15:
        print(lista[i][0],lista[i][1])
    
    

    
