def spolgloski(x):#zlicza spolgloski, jesli znajdzie samogloske, zeruje licznik
     s=0
     ciag=0
     for i in range(len(x)):
          if x[i]=='A' or x[i]=='O' or x[i]=='I' or x[i]=='E' or x[i]=='U' or x[i]=='Y':
               s=0
          else:
               s+=1
          if s>ciag:#znajduje najdłuższy ciąg spółgłosek w wyrazie
               ciag=s
     return ciag

file=open("tekst.txt","r")
linia=[]
line=file.readline().strip()#odczytanie całej linii i wrzucenie pojedynczych słów na listę
linia=line.split()

najdluzsze=0
for x in linia:
     k=spolgloski(x)
     if k>najdluzsze:
          najdluzsze=k
          licznik=1
          odpowiedz=x
     elif k==najdluzsze:
          licznik+=1
          
     
print('Najdłuższe podsłowo',najdluzsze)
print('Ilosc słów',licznik)
print(odpowiedz)

     

