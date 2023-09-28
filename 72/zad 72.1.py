lista=[]
licznik=0
file=open("napisy.txt","r")
for x in file:
    x=x.strip()
    lista.append(x.split())

for i in range(200):
    dl1=len(lista[i][0])
    dl2=len(lista[i][1])
    if dl1>=3*dl2 or dl2>=3*dl1:
        licznik+=1
        if licznik==1:
            print(lista[i])
    
print(licznik)
