file=open('dane_geny.txt','r')
lista=[]
lista_genow=[]
dl_gen=[]
licznik=0


for x in file:
    x=x.strip()
    i=0
    il_genow=0
    while i<len(x)-4:
        nowy=''
        if x[i]=='A' and x[i+1]=='A':
            indeks=i
            i+=2
            while (x[i]!='B' or x[i+1]!='B') and i<len(x)-4:
                i+=1
            if x[i]=='B' and x[i+1]=='B':
                koniec=i+2
                gen=x[indeks:koniec]
                dl_gen.append(len(gen))
                lista.append(gen)
                il_genow+=1
        i+=1
    lista_genow.append(il_genow)
       
print(max(lista_genow))
print(max(dl_gen))

