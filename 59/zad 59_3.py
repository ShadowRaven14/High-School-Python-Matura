def rozklad_na_cyfry(a):
    iloczyn=1
    while a>0:
        reszta=a%10
        iloczyn*=reszta
        a=a//10
    return iloczyn

def ciag(n):
    moc=0
    while n>9:
        n=rozklad_na_cyfry(n)
        moc+=1
    return moc     

file=open('liczby.txt','r')
lista=[]
liczby=[]
slownik={}
ilosc1=0
ilosc2=0

for x in file:
    x=x.strip()
    liczba=int(x)
    lista.append(liczba)

for x in lista:
    moc=ciag(x)
    if moc>0 and moc<9:
        if moc in slownik:
            slownik[moc]+=1 #jesli element wystepuje zzwiekszamy licznik o 1
        else:
            slownik[moc]=1 #jesli nie wystepuje tworzymy go i ustawiamy na 1
        if moc==1:
            liczby.append(x)
        
print(slownik)
print('Min',min(liczby),'Max',max(liczby))

