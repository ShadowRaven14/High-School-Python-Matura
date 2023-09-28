def trojkat(a,b,c):
    if ((a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b)):
        return True
    else:
        return False


file=open("trojki.txt","r")
lista=[]

for x in file:
    x=x.strip()
    lista.append(x.split())

for i in range(999):
    pierwszy=trojkat(int(lista[i][0]),int(lista[i][1]),int(lista[i][2]))
    drugi=trojkat(int(lista[i+1][0]),int(lista[i+1][1]),int(lista[i+1][2]))
    if pierwszy and drugi:
        print (lista[i])
        print(lista[i+1])

