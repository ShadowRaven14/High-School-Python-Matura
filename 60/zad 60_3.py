def nwd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a      
    if a!=0:
        return a
    else:
        return b

def szukam(i):
    for j in range(i+1,200):
        if nwd(lista[i],lista[j])!=1:
            return False
    return True

file=open('liczby.txt', 'r')
lista=[]
for x in file:
    x=x.strip()
    lista.append(int(x))
        
nowe=[]
for i in range(200):
    if szukam(i):
        nowe.append(lista[i])

print(max(nowe))
