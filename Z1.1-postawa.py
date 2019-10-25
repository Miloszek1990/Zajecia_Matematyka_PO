#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 08:40:34 2019

@author: Miłosz
"""
### Instrukcja if
print("!!! 1. Instrukcja if.")
var_int = 1
var_str = "kkk"
var_lst = [1,2,"kkk"]

#
if var_int == 1:
    print("That int")

#
if var_str == "kkk":
    print("That string")

#
if var_lst == [1,2,"kkk"]:
    print("That list")
elif var_lst == [1,2,"kkk","kkk"]:
    print("That 2nd list")
else:
    print("No list :(")

### Pętla for
# Podstawa 1
print("!!! 2. Pętla for - podstawa 1.")
for i in range(10):
    print(i)

print("!!! 3. Pętla for - podstawa 2.")
# Podstawa 2
for element in var_lst:
    print(element)

print("!!! 3. Pętla for - generowanie zmiennych")
# Robienie list
lst_1 = []
for parzyste in range(0, 10, 2):
    lst_1.append(parzyste)

lst_2 = [parzyste for parzyste in range(0, 10, 2)]

# Robienie słowników
dct_1 = {}
for i, parzyste in enumerate(range(0, 10, 2)):
    dct_1[i] = parzyste

dct_2 = {i : parzyste for i, parzyste in enumerate(range(0, 10, 2))}

### Definiowanie własnych funkcji
# Podstawa
print("!!! 4. Funkcje - podstawa 1")
def pitagoras(a,b):
    c = (a**2 + b**2)**0.5
    return c
print(pitagoras(2,2))

# Podstwa z podpowiedziami wejścia wyjścia
print("!!! 4. Funkcje - podstawa 2 - SUGESTIE wejścia, wyjścia")
def suma(a : int,
         b : int) -> (int, int, int):
    
    c = a + b
    
    return a, b, c

aa, bb, cc = suma(2,3)
print(aa)
print(bb)
print(cc)