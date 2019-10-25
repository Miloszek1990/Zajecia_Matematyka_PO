#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:52:09 2019

@author: foton
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('./Lenna.png')

img_R = np.matrix((img[:,:,0] * 255)).astype(int)
img_G = np.matrix((img[:,:,1] * 255)).astype(int)
img_B = np.matrix((img[:,:,2] * 255)).astype(int)

### Generowanie histogramów
#
# 1. Skorzystaj z powyrzszego kodu aby załadować 
#    i znormalizować do 8-bitów obraz Lenny
#
# 2. Napisz funkje, która będzie przyjmować 2 argumenty
#    a) Numpy macierz z warstwą obrazu/obrazem
#    b) Wartość logiczną czy normalizować histogram
#
# 2.1 Funkcja ma zliczyć piksele danej wartości
#    i zapisać je do słownika. Zliczanie ma być
#    wykonane za pomocą klucz-wartość aby maksymalnie
#    obniżyć koszt obliczeniowy.
#    Funkcja ma mieć wydajność algorytmiczną 
#    O(n)! a nie np. O(N^2)
#    
# 2.2 W przypadku normalizacji podziel wszystkie
#    słupki przez ilość wszystkich pikseli 
#
# 3. Wywołaj funkcje na każdej warstwie obrazu i 
#    zapisz je w liście.
#
# 4. Napisz funkcje która wygeneruje wykres słupkowy
#    typu plt.bar() i zwróci 3 wykresy na jednej figurze.
#
# 4.1 Zadbaj o styl prezentacji danych.
# 
# 4.2 Funkcja ma przyjmować listę histogramów i wartość
#    logiczną dotyczącą zapisywania wykresu.
