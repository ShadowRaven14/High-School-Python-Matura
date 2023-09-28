def czynniki(a):
    dziel=3
    ile=0
    
    if a%2==0:
        return False
    while a>1:
        if a%dziel==0:
            ile+=1
        while a%dziel==0:
            a=a//dziel
        dziel+=2
        if ile>3:
            return False
    if ile==3:
        return True
    elif ile<3:
        return False
            


file=open('liczby.txt','r')
ilosc=0

for x in file:
    x=x.strip()
    liczba=int(x)
    if czynniki(liczba):
        ilosc+=1
print(ilosc)
