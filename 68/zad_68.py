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

file=open('dane_napisy.txt','r')

licznik=0

for x in file:
    x=x.strip()
    lista=x.split()
    if anagram(lista[0],lista[1]):
        licznik+=1
print(licznik)
