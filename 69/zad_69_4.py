def genotyp_odporny(x):
    gen=''
    i=0
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
                #lista.append(gen)
                print(gen)
        i+=1
    return gen
    
file=open('dane_geny.txt','r')
lista=[]

silnie_odporny=0
odporny=0


for x in file:
    x=x.strip()
    if x==x[::-1]:
        silnie_odporny+=1
    y=x[::-1]
    if genotyp_odporny(x)==genotyp_odporny(y):
        odporny+=1
       
print(silnie_odporny)
print(odporny)

