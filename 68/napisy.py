print("Czy długości wyrazów w zdaniach są jednakowe:")

lista_anagramow = []
with open("dane_napisy.txt") as znaki:
  for wers in znaki:
    wers = wers.strip()
    para = wers.split()
    lista_anagramow.append(para)

def jest_anagramem(ciag, ciag1):
    if len(ciag) == len(ciag1):
        a = set(ciag[::])
        b = set(ciag1[::])
        if a == b:
            return True
    return False

def liczba_k():
    k = 0
    wyrazy = []
    for para in lista_anagramow:
        wyrazy.append(para[0])
        wyrazy.append(para[1])
    for sprawdzany_wyraz in wyrazy:
        zliczanie = 0
        for ciag in wyrazy:
            if jest_anagramem(sprawdzany_wyraz, ciag):
                zliczanie += 1
            if zliczanie > k:
                k = zliczanie
    return k

print("Szukana liczba k: " + str(liczba_k()))
