def anagram(s1,s2):
    if len(s1)==len(s2):
        if jednolity(s1) and jednolity(s2):
            return True
        else:
            return False
    else:
        return False


def jednolity(s):
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            return False
    return True
            
           
file=open('dane_napisy.txt','r')

licznik=0

for x in file:
    x=x.strip()
    lista=x.split()
    if anagram(lista[0],lista[1]):
        licznik+=1

print(licznik)
