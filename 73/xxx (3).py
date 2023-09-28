import random
import math

# 20 liczb wylosowac zsumowac parzyste i nieparzyste
'''even, odd = 0, 0
for i in range (20):
	number = random.randint(1,20)
	if(number%2==0):
		even+=number
	else:
		odd+=number
print("suma parzystych to: "+str(even)+" suma nieparzystych to: "+str(odd))'''

# rozklad na czynniki pierwsze
'''number, x = int(input("podaj liczbe ")), 2
while number!=1:
	if number%x==0:
		print(x)
		number/=x
	else:
		x+=1'''


# czy liczba pierwsza
def is_prime(number):
    if number <= 1:
        return False
    if type(number) != int:
        return False
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


# czynniki pierwsze
def prime_factors(number):
    x = 2
    y = 0
    while number != 1:
        if number % x == 0:
            y += 1
            number /= x
        else:
            if (y != 0):
                print(x, '^', y)
            x += 1
            y = 0
    print(x, '^', y)


def is_half_prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            number //= i
            if isPrime(number):
                return True
            else:
                return False
    return False


# 4 poczatkowe liczby doskonale, suma wszystkich swoich dzielnikow wlasciwych 6, 28
def is_perfect_number(number):
    sum = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            sum += i
            print(i)
    if sum == number:
        return True
    return False


# znajdz 3 poczatke pary liczb zaprzyjaznionych 220 i 284 suma dzielnikow jest 1184 1210 5020 5564
def suma_skladnikow(number):
    sum = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            sum += i
    return sum


def is_friendly_number(number1, number2):
    if suma_skladnikow(number1) == number2 and suma_skladnikow(number2) == number1:
        return True
    return False


def convert_from_x_to_decimal(number1, base):
    pow, num, alf = len(number1) - 1, 0, 'ABCDEF'
    for x in number1:
        if x.isalpha():
            num += (10 + alf.index(x)) * base ** pow
        elif int(x) > 0:
            num += int(x) * base ** pow
        pow -= 1
    return num


def convert_from_decimal_to_base_x(number1, base):
    number1, result, alf = int(number1), '', 'ABCDEF'
    while number1 // base != 0:
        if number1 % base > 9:
            result += alf[number1 % base - 10]
        else:
            result += str(number1 % base)
        number1 //= base

    if number1 % base > 9:
        result += alf[number1 % base - 10]
    else:
        result += str(number1 % base)
    return result[::-1]


def compute_primes(n):
    list = [True] * (n + 1)
    for i in range(2, n + 1):
        if list[i]:
            for x in range(i * i, n + 1, i):
                list[x] = False
    return list


def is_square_of_prime(n):
    x = math.sqrt(n)
    if x % 1 == 0:
        if is_prime(int(x)):
            return True
    return False


# liczby lustrzane - para liczb pierwszych ktore maja odwrocone cyfry np 17 i 71
def are_mirrored_primes(n1, n2):
    if is_prime(n1) and is_prime(n2):
        n2 = str(n2)
        n2 = n2[::-1]
        n2 = int(n2)
        if n1 == n2:
            return True
    return False


def zadanie1(list):
    n = 0
    for i in range(1, len(list)):
        if list[i - 1] != list[i]:
            n += 1
    return n


def zadanie2(list):
    numA, numB = 0, 0
    for ch in list:
        if ch == 'A':
            numA += 1
        else:
            numB += 1
        if numA > 999 or numB > 999:
            if abs(numA - numB) > 2:
                if numA > numB:
                    winner = 'A'
                else:
                    winner = 'B'
                return (winner + ' ' + str(numA) + ':' + str(numB))


def zadanie3(list):
    passa_sum = 0
    current_passa_len = 1
    passa_holder = 'A'
    longest_passa = 9
    longest_passa_holder = ''
    for ch in list:
        if passa_holder == ch:
            current_passa_len += 1
        else:
            passa_holder = ch
            current_passa_len = 1
        if current_passa_len == 10:
            passa_sum += 1
        if current_passa_len > longest_passa:
            longest_passa = current_passa_len
            longest_passa_holder = passa_holder
    print(passa_sum, ' ', longest_passa_holder, ' ', longest_passa)


def horner(stopien, wsp, x):
    wynik = wsp[0]
    for i in range(1, stopien + 1):
        wynik = wynik * x + wsp[i]
    return wynik


def any_to_decimal_horner(num, base):
    wsp = []
    for i in num:
        wsp.append(int(i))
    stopien = len(num) - 1
    return horner(stopien, wsp, base)


def silnia(num):
    if num < 2:
        return 1
    else:
        return silnia(num - 1) * num


def digits(num):
    if num < 10:
        print(num)
    else:
        digits(num // 10)
        print(num % 10)


def potegowanie_rekurencyjne(x, n):
    if n == 1:
        return x
    tmp = potegowanie_rekurencyjne(x, n // 2)
    tmp *= tmp
    if n % 2 == 1:
        tmp *= x
    return tmp


def fibbonaci_rekurencyjny(x):
    if x < 3:
        return 1
    return fibbonaci_rekurencyjny(x - 1) + fibbonaci_rekurencyjny(x - 2)


def fibbonaci_iteracyjny(x):
    sum = 2
    first = 1
    second = 1
    for i in range(x - 2):
        l = first + second
        first = second
        second = l
        sum += l
    print(l, ' ', sum)


def bubble_sort(list):
    finished = False
    while not finished:
        finished = True
        for i in range(1, len(list)):
            if list[i - 1] > list[i]:
                finished = False
                n = list[i - 1]
                list[i - 1] = list[i]
                list[i] = n
    return list


def sum_of_digits(x):
    x, n = str(x), 0
    for ch in x:
        n += int(ch)
    return n


def sortowanie1(list):
    finished = False
    while not finished:
        finished = True
        for i in range(1, len(list)):
            a = str(list[i - 1])
            c = int(a[-1])
            b = str(list[i])
            d = int(b[-1])
            if c > d:
                finished = False
                n = list[i - 1]
                list[i - 1] = list[i]
                list[i] = n
    return list


def sortowanie2(list):
    finished = False
    while not finished:
        finished = True
        for i in range(1, len(list)):
            c = sum_of_digits(list[i - 1])
            d = sum_of_digits(list[i])
            if c > d:
                finished = False
                n = list[i - 1]
                list[i - 1] = list[i]
                list[i] = n
    return list


def count_ones_in_binary(num):
    x = convert_from_decimal_to_base_x(num, 2)
    result = 0
    for ch in x:
        if ch == "1":
            result += 1
    return result


def sortowanie3(list):
    finished = False
    while not finished:
        finished = True
        for i in range(1, len(list)):
            if count_ones_in_binary(list[i - 1]) < count_ones_in_binary(list[i]):
                finished = False
                n = list[i - 1]
                list[i - 1] = list[i]
                list[i] = n
    return list


def sortowanie4(list):
    odd = []
    even = []
    for num in list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd + even


def sortowanie5(list):
    for i in range(1, len(list)):
        key = list[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if list[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, left - 1, -1):
            list[j + 1] = list[j]
        list[left] = key
    return list


def smallest_prime_factor(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i
    return n


def sortowanie6(list):
    finished = False
    while not finished:
        finished = True
        for i in range(1, len(list)):
            if smallest_prime_factor(list[i - 1]) > smallest_prime_factor(list[i]):
                finished = False
                n = list[i - 1]
                list[i - 1] = list[i]
                list[i] = n
    return list


def check_first_last_digit (n):
    n = str(n)
    if n[0] == n[-1]:
        return True
    return False


def check_if_every_digit_is_greater (n):
    n = str(n)
    for i in range (1, len(n)):
        if int(n[i-1]) > int(n[i]):
            return False
    return True


def zadanie2 ():
    for i in range (100, 200):
        n = str(i)
        end = True
        for x in range (1, len(n)):
            if int(n[x-1]) >= int(n[x]):
                end = False
        if end:
            print(i)


def is_superprime (n):
    if is_prime(n) and is_prime(sum_of_digits(n)):
        return True
    return False


def fun_with_strings (str):
	print(str.upper())
	print(str.lower())
	print(str.strip())
	print(str.replace('a','b'))
	print(str.split(','))
	print(str.find('o'))
	print(str.index('o'))
	print(chr(65))

def palindrome_word (str):
    if str == str[::-1]:
        return True
    return False

def palindrome_sentence (str):
    str = str.lower()
    for ch in str:
        if not ch.isalpha():
            str = str.replace(ch,'')
    return palindrome_word(str)

def devide_letters_digits (str):
    letters, digitss = '', ''
    for ch in str:
        if ch.isalpha():
            letters += ch
        if ch.isdigit():
            digitss += ch
    return letters, digitss

def count_words (str):
    str = str.strip()
    words = 1
    for ch in str:
        if ch == ' ':
            words += 1
    return words

def count_letters (str):
    letters = 0
    for ch in str:
        if ch.isalpha():
            letters += 1
    return letters

def is_anagram (str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = str1.strip()
    str2 = str2.strip()
    if sorted(str1) == sorted(str2):
        return True
    return False

#wszystkie wyrazy ta sama liczba liter
def is_every_word_same_length (str):
    words = str.split()
    for x in range (1, len(words)):
        if len(words[x-1]) != len(words[x]):
            return False
    return True

def all_letters_same (text):
    letter = text[0]
    for x in text:
        if x != letter:
            return False
    return True

def zadanie681 (text):
    result = 0
    text = text.split()
    for i in range (0,len(text)-1,2):
        if text[i] == text[i+1]:
            result += 1
    return result

def zadanie682 (text):
    result = 0
    text = text.split()
    for i in range(0, len(text) - 1, 2):
        if is_anagram(text[i],text[i+1]):
            result += 1
    return result


def zadanie683 (text):
    text = text.split()
    list = [False]*len(text)
    k = 0
    l = 0
    finished = False
    while not finished:
        l = 0
        finished = True
        if False in list:
            lowestFalse = list.index(False)
            word = text[lowestFalse]
            for x in range(lowestFalse, len(text)):
                if not list[x]:
                    finished = False
                    if is_anagram(text[x], word):
                        l += 1
                        list[x] = True
            if l > k:
                k = l
    return k

def zadanie691 (text):
    text = text.split()
    gatunki = [0]*500
    for gatunek in text:
        gatunki[len(gatunek)] += 1
    ilosc = 0
    for x in gatunki:
        if x > 0:
            ilosc += 1
    maximum = max(gatunki)
    return ilosc, maximum

def get_genes(text):
    geny = []
    for genotyp in text:
        while 'AA' in genotyp and 'BB' in genotyp:
            aa = genotyp.index('AA')
            bb = genotyp.index('BB')
            if aa < bb:
                geny.append(genotyp[aa:bb+2])
            genotyp = genotyp[bb+2:]
    return geny

def zadanie692 (text):
    text = text.split()
    num = 0
    geny = get_genes(text)
    for gen in geny:
        if 'BCDDC' in gen:
            num += 1
    return num

def zadanie693 (text):
    text = text.split()
    lenght = [0]*len(text)
    for i in range (len(text)):
        genotyp = text[i]
        while 'AA' in genotyp and 'BB' in genotyp:
            aa = genotyp.index('AA')
            bb = genotyp.index('BB')
            if aa < bb:
                lenght[i] += 1
            genotyp = genotyp[bb+2:]
    geny = get_genes(text)
    lenght2 = []
    for gen in geny:
        lenght2.append(len(gen))
    return max(lenght), max(lenght2)

def zadanie694 (text):
    text = text.split()
    x = 0
    geny = get_genes(text)
    for genotyp in text:
        if genotyp == genotyp[::-1]:
            x += 1
    y = 0
    for genotyp in text:
        geny1 = []
        geny2 = []
        genotyp2 = genotyp[::-1]
        while 'AA' in genotyp and 'BB' in genotyp:
            aa = genotyp.index('AA')
            bb = genotyp.index('BB')
            if aa < bb:
                geny1.append(genotyp[aa:bb+2])
            genotyp = genotyp[bb+2:]
        while 'AA' in genotyp2 and 'BB' in genotyp2:
            aa = genotyp2.index('AA')
            bb = genotyp2.index('BB')
            if aa < bb:
                geny2.append(genotyp2[aa:bb+2])
            genotyp2 = genotyp2[bb+2:]
        if geny1 == geny2:
            y += 1
    return x , y

def zadanie661 (text):
    for i in range (0, 2999, 3):
        if sum_of_digits(text[i]) + sum_of_digits(text[i+1]) == text[i+2]:
            print(text[i],' ',text[i+1],' ',text[i+2])

def zadanie662 (text):
    for i in range (0, 2999, 3):
        if is_prime(text[i]) and is_prime(text[i+1]) and text[i] * text[i+1] == text[i+2]:
            print(text[i],' ',text[i+1],' ',text[i+2])

def make_right_triangle(a,b,c):
    a, b, c = a*a, b*b, c*c
    if a + b == c or a + c == b or b + c == a:
        return True
    return False

def make_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def zadanie663 (text):
    for i in range (0, 2996, 3):
        if make_right_triangle(text[i], text[i+1], text[i+2]):
            if make_right_triangle(text[i+3], text[i+4], text[i+5]):
                print(text[i], ' ', text[i + 1], ' ', text[i + 2])
                print(text[i+3], ' ', text[i + 4], ' ', text[i + 5])
                print()

def zadanie664 (text):
    longest, current, all = 0, 0, 0
    for i in range (0, 2999, 3):
        if make_triangle(text[i], text[i+1], text[i+2]):
            current += 1
            all += 1
            if current > longest:
                longest = current
        else:
            current = 0
    return all, longest

def zadanie721 (text):
    n = 0
    first_pair_found = False
    for i in range (0,399,2):
        a, b = len(text[i]), len(text[i+1])
        if a >= 3*b or b >= 3*a:
            n += 1
            if not first_pair_found:
                first_pair = text[i] + ' ' + text[i+1]
                first_pair_found = True
    return first_pair, n

def zadanie722 (text):
    for i in range (0,399,2):
        word1, word2 = text[i], text[i+1]
        if word1 == word2[:len(word1)]:
            print(word1,' ',word2,' ',word2[len(word1):])

def find_length_of_same_first_letters (word1, word2):
    a, b = len(word1), len(word2)  # znajdowanie mniejszej dlugosci dla fora
    if a < b:
        a = b
    length = 0
    for l in range(a):
        if word1[l] == word2[l]:
            length += 1
        else:
            return length

def zadanie723 (text):
    max_length = 0
    for i in range (0,399,2):
        word1, word2 = text[i], text[i+1]
        word1, word2 = word1[::-1], word2[::-1]
        length = find_length_of_same_first_letters(word1, word2)
        if length > max_length:
            max_length = length
    print (max_length)
    for i in range(0, 399, 2):
        word1, word2 = text[i], text[i+1]
        word1, word2 = word1[::-1], word2[::-1]
        word3, word4 = word1[:max_length], word2[:max_length]
        if word3 == word4:
            print(word1[::-1],' ',word2[::-1])

def zadanie731 (text):
    x = 0
    for word in text:
        l = len(word)-1
        for i in range(l):
            if word[i] == word[i+1]:
                x += 1
                break
    return x

def zadanie732 (text):
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = ''.join(text)
    text = text.replace(' ','')
    num_letters = len(text)
    for letter in alf:
        n = text.count(letter)
        print(letter, n, round(n / num_letters * 100, 2), '%')


def zadanie733 (text):
    sam = 'AEIOUY'
    big_l = 0
    big_s = ''
    for word in text:
        cur_l = 0
        cur_s = ''
        for letter in word:
            if letter in sam:
                cur_l = 0
                cur_s = ''
            else:
                cur_l += 1
                cur_s += letter
            if cur_l > big_l:
                big_l = cur_l
                big_s = cur_s
    num = 0
    for word in text:
        if big_s in word:
            num += 1
            print(word)
    print(big_s,num,big_l)

#kod główny
file = open('tekst.txt','r')
text = file.read()
text = text.strip()
text = text.split()
print(zadanie731(text))
zadanie732(text)
zadanie733(text)
