def dziel(a):
    dzielniki=[]
    for i in range(1,a+1):
        if a%i==0:
            dzielniki.append(i)
    if len(dzielniki)==18:
        print(a)
        print(sorted(dzielniki))
            


file=open('liczby.txt','r')
lista=[]
for x in file:
    x=x.strip()
    lista.append(int(x))
  
for x in lista:
    dziel(x)
    
