def anagram(s1,s2):
    if len(s1)==len(s2):
        s1=sorted(s1)
        s2=sorted(s2)
        if s1==s2:
            return True
        else:
            return False
    else:
        return False
def dodaj(a):
    a=sorted(a)
    wyraz=''
    for x in a:
        wyraz+=x
    return wyraz
file=open('dane_napisy.txt','r')
k=0
licznik=0
wyraz=''
lista_anagramow=[]
for x in file:
    x=x.strip()
    lista=x.split()
    if anagram(lista[0],lista[1]):
        lista_anagramow.append(dodaj(lista[0]))
        lista_anagramow.append(dodaj(lista[1]))
print(lista_anagramow)
print(len(lista_anagramow))
for i in range(len(lista_anagramow)):
    n=lista_anagramow.count(lista_anagramow[i])
    if n>k:
        k=n
print(k)
        
