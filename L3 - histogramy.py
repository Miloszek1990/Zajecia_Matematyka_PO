#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:52:09 2019

@author: foton
"""
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
import polib as po

import matplotlib.pyplot as plt

def set_two_ticks(axes):
    ymin, ymax = axes.get_ylim()
    axes.set_yticks([round((ymax-ymin)/2,2)])

def plot_histograms(histogram, save=False):   
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    
    ax1.bar(list(histogram[0].keys()), histogram[0].values(), color='r')
    ax2.bar(list(histogram[1].keys()), histogram[1].values(), color='g')
    ax3.bar(list(histogram[2].keys()), histogram[2].values(), color='b')

    set_two_ticks(ax1)
    set_two_ticks(ax2)
    set_two_ticks(ax3)
    
    ax2.set_ylabel("Pixels number [-]")
    ax3.set_xlabel("Pixel count [-]")
    
    fig.subplots_adjust(hspace=0)
    if save == True:
        plt.savefig('hist.png', bbox_inches='tight', format='png', dpi=500)

bits = 8
img_path = "../Lenna.png"

img_R = po.read_image_matplotlib(img_path, bits, 0)
img_G = po.read_image_matplotlib(img_path, bits, 1)
img_B = po.read_image_matplotlib(img_path, bits, 2)

hist_R = po.histogram(img_R, bits, False)
hist_G = po.histogram(img_G, bits, False)
hist_B = po.histogram(img_B, bits, False)

his = [hist_R, hist_G, hist_B]
plot_histograms(his, False)
