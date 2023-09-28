dane = open("dane_geny.txt", "r")

gatunki = []
gen = ""
genotyp_skrocony = ""
licznik = 0
geny = []
for genotyp in dane:
    genotyp = genotyp[:-1]

    stop = 0
    while stop != 1:
        if "AA" in genotyp and "BB" in genotyp:
            x = genotyp.find('AA')
            y = genotyp.find('BB')
            if y < x:
                genotyp_skrocony = genotyp[x:]
                x = genotyp_skrocony.find('AA')
                y = genotyp_skrocony.find('BB')
            gen = genotyp_skrocony[x:y + 2]
            geny.append(gen)
            genotyp = genotyp[y+2:]
        else:
            stop = 1
print(geny)
for gen in geny:
    if "BCDDC" in gen:
        licznik += 1
print(licznik)