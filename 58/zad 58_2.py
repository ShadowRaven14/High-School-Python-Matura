 
def na_dziesietny(a,podst):
     dzies=0
     znak=1
     if a[0]=='-':
          a=a[1:] #obcinam minus
          znak=-1
     a=a[::-1] #obracam napis
     for i in range(len(a)):
          dzies=dzies+int(a[i])*podst**i

     return dzies*znak


def stany(czas1, czas2, czas3):
     stan=12
     licz=0
     for i in range(1095):
          if czas1[i]!=stan and czas2[i]!=stan and czas3[i]!=stan:
               licz+=1
          stan=stan+24
     return licz
     

file1=open('dane_systemy1.txt','r')
file2=open('dane_systemy2.txt','r')
file3=open('dane_systemy3.txt','r')

temp1=[]
temp2=[]
temp3=[]
czas1=[]
czas2=[]
czas3=[]

for x in file1:
     x=x.strip()
     lista=x.split()
     temp1.append(na_dziesietny(lista[1],2))
     czas1.append(na_dziesietny(lista[0],2))

for x in file2:
     x.strip()
     lista=x.split()
     temp2.append(na_dziesietny(lista[1],4))
     czas2.append(na_dziesietny(lista[0],4))

for x in file3:
     x.strip()
     lista=x.split()
     temp3.append(na_dziesietny(lista[1],8))
     czas3.append(na_dziesietny(lista[0],8))

print(stany(czas1, czas2, czas3))
