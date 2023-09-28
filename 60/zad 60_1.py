file=open('liczby.txt', 'r')
lista=[]
licz=0
for x in file:
    x=x.strip()
    lista.append(int(x))
lista=lista[::-1]
for i in range(200):
    if lista[i]<1000:
        licz+=1
        if licz<3:
            print(lista[i])
print('Ilość ',licz)
