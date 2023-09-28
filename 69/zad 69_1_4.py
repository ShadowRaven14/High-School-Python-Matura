z = int(input("numer zadania: "))
#207 i 20
if z == 1:
    f = open ("dane_geny.txt", "r")
    tab = [" "] 
    suma, a = 0, 0
    znaki = f.read()
    znaki = znaki.split () 
    for i in znaki:
        tab. append (len(i))
    tab. pop (0)
    ta= [0]*len(tab)
    for i in tab:
        ta[i] += 1
    for i in ta:
        if i != 0:
            suma += 1
        if i > a:
            a = i

    print (suma)
    print(a)

#8, bez ostatniego C - 43
if z == 2:
    f = open ("dane_geny.txt", "r")
    c = "" 
    suma, a, b  = 0, 0, 0
    znaki = f.read()
    znaki = znaki.split()
    tab = [""]
    for i in range(len(znaki)):
        a, b = 0, 0 
        while a != -1 and b != -1:
            b = znaki[i].find ("BB")
            a = znaki[i].find("AA") 
            if a != -1 or b != -1:
                c = znaki[i][a:b+2]
                znaki[i] = znaki[i][b+2:]
                tab.append (c)

    for i in tab:
        a = i.find ("BCDDC")
        if a != -1:
            suma += 1 
            print (i)               
    print (suma)

#11
if z == 3:        
    f = open ("dane_geny.txt", "r")
    c = "" 
    suma, suma1, d = 0, 0, 0
    znaki = f.read()
    znaki = znaki.split()
    tab = [""]
   
    for i in range(len(znaki)):
        a, b, d = 0, 0, 0 
        while a != -1 and b != -1:
            b = znaki[i].find ("BB")
            a = znaki[i].find("AA") 
            if a != -1 and b != -1:  
                if b>a:
                    c = znaki[i][a:b+2]
                    tab.append (c)
                    d+=1
            znaki[i] = znaki[i][b+2:]
        if suma1 < d:
            suma1 = d

            
    tab1 = [""]*len(tab)
    c = 0

    for i in range(len(tab)):
        tab1[i] = len(tab[i])

    for i in tab1:
        if  i > c:
            c = i
    print ("największa ilość genów u osobnika: " +str(suma1)) 
    print ("najdłuższy gen: " + str(c))
#187, 249
if z == 4:
    f = open ("dane_geny.txt", "r")
    c = "" 
    suma, suma1, d = 0, 0, 0
    znaki = f.read()
    znaki = znaki.split()
    zn = znaki
    tab = [""]
    tab1= [""]
   
    for i in range(len(zn)):
        a, b = 0, 0  
    for i in zn:
        if i == i[::-1]:
            suma  += 1
    print ("gen silnie odporny: " + str(suma))

    for i in range(len(znaki)):
        a, b = 0, 0 
        
        while a != -1 and b != -1:
            b = znaki[i].find("BB")
            a = znaki[i].find("AA")
            if a != -1 and b != -1:   
                if b>a:
                    c = znaki[i][a:b+2]
                    tab1.append (c)
            znaki[i] = znaki[i][b+2:]
        
        a,b=1,1

        f = open ("dane_geny.txt", "r")
        zna= f.read()
        zna = zna.split()
        e = zna[i][::-1]

        while a != -1 and b != -1:                
            b = e.find ("BB")
            a = e.find("AA") 
            if a != -1 and b != -1:     
                if b>a:
                    c = e[a:b+2]                   
                    tab.append(c)
            e = e[b+2:]

        tab = sorted(tab)
        tab1 = sorted(tab1)
        if tab1 == tab:
            suma1+=1
   
        tab.clear() 
        tab1.clear()    

print ("geny odporne" + str(suma1))