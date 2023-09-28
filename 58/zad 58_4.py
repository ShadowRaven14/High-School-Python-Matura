   
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

def skoki(temp1):
     maks=0
     
     for i in range(1094):
          for j in range(i+1,1095):
               kwadrat=pow(temp1[i]-temp1[j],2)
               skok=kwadrat//(j-i)
               if kwadrat%(j-i)!=0:
                    skok=skok+1
               if skok>maks:
                    maks=skok
     return maks
               
               

file1=open('dane_systemy1.txt','r')

temp1=[]

for x in file1:
     x=x.strip()
     lista=x.split()
     temp1.append(na_dziesietny(lista[1],2))

print(skoki(temp1))
