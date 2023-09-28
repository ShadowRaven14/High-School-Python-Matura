lista=[]
licznik=0
file=open("napisy.txt","r")
for x in file:
    x=x.strip()
    lista.append(x.split())

for i in range(200):
    a=lista[i][0]
    b=lista[i][1]
    if len(a)<len(b):
        s=b[0:len(a)]
        if a==s:
            print(a,b,b[len(a):len(b)])
    
