 
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

def na_dwojkowy(b):
     zn=''
     dw=''
     if b<0:
          zn='-'
          b=b*(-1)
     while b>0:
          dw=dw+str(b%2)
          b=b//2
     dw=dw[::-1]
     dw=zn+dw
     return dw

        

file1=open('dane_systemy1.txt','r')
file2=open('dane_systemy2.txt','r')
file3=open('dane_systemy3.txt','r')

temp1=[]
temp2=[]
temp3=[]

for x in file1:
     x=x.strip()
     lista=x.split()
     temp1.append(na_dziesietny(lista[1],2))

print(na_dwojkowy(min(temp1)))

for x in file2:
     x.strip()
     lista=x.split()
     temp2.append(na_dziesietny(lista[1],4))

print(na_dwojkowy(min(temp2)))

for x in file3:
     x.strip()
     lista=x.split()
     temp3.append(na_dziesietny(lista[1],8))

print(na_dwojkowy(min(temp3)))

