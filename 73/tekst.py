def zad1():
    file = open('tekst.txt','r')
    suma = 0
    tab = []
    for x in file:
        x = x.strip()
        tab = x.split(' ')
        for i in tab:
            for j in range (0, len(i)-1):
                if i[j] == i[j+1]:
                    suma += 1
    print('zad1: ',suma)
    print('')

def zad2():
    file = open('tekst.txt','r')
    litery = 0
    tab = []
    t = 91*[0]
    print('zad2:')
    for x in file:
        x = x.strip()
        tab = x.split(' ')
        for i in tab:
            for j in range (65, 91):
                for k in range(0, len(i)):
                    if i[k] == chr(j):
                        t[ord(i[k])] += 1      
            litery += len(i)
    for i in range (65, 91):
        print(chr(i), ':',t[i],'(',round((t[i]/litery)*100,2),'%',')')
    print('')

def zad3():
    file = open('tekst.txt','r')
    tab = []
    print('zad3: ')
    maks = 0
    k = 1
    liczba = 0
    pom = ''
    for x in file:
        x = x.strip()
        tab = x.split(' ')
        for i in tab:
            t = []
            i = i.replace('A',' ')
            i = i.replace('E',' ')
            i = i.replace('I',' ')
            i = i.replace('O',' ')
            i = i.replace('U',' ')
            i = i.replace('Y',' ')
            t = i.split(' ')
            for j in t:
                if len(j) > maks:
                    maks = len(j)
    print('dlugosc najdluzszego podslowa: ',maks)
    for i in tab:
        pom = i
        t = []
        i = i.replace('A',' ')
        i = i.replace('E',' ')
        i = i.replace('I',' ')
        i = i.replace('O',' ')
        i = i.replace('U',' ')
        i = i.replace('Y',' ')
        t = i.split(' ')
        for j in t:
            if len(j) == maks and k == 1:
                print('pierwsze slowo zawierajace podslowo o takiej dlugosci: ',pom)
                k = 0
            if len(j) == maks:
                liczba += 1
                break
    print('Liczba slow zawierajacych podslowa o takiej dlugosci',liczba)
                                     
zad1()
zad2()
zad3()

