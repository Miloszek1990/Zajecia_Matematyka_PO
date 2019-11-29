#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:20:22 2019

@author: foton
"""
import polib as po
import numpy as np
### POLIB - Przetwarzanie Obrazów LIBrary
### FUNKCJE POMOCNICZE
### - Wczytanie N-bitowego obrazka (matplotlib)
### - Sprawdzenie wielkości jądra
### - Wygenerowanie N-bitowej zaszumonej numpy macierzy (obrazka)
### - TODO - Wygenerowanie obrazka sinusa
### 
### FUNKCJE ANALIZUJĄCE
### - Oblicz histogram obrazka
### - Oblicz entropie obrazka z jego histogramu
### 
### FUNKCJE FILTRUJĄCE
### FILTRACJA BEZKONTEKSTOWA
### - Binaryzacja globalna
### 
### FILTRACJA KONTEKSTOWA
### - Binaryzacja adaptacyjna
###     - Średnia
###     - Mediana
###     - TODO - Gauss

bits = 15
img_size = (180, 150)
img_info = (img_size[0], img_size[1], bits)

### WYGENERUJ ZASZUMIONY N-bioty obraz
img = po.noise_image(img_size, bits)

### OBLICZ JEGO HISTOGRAM
img_hist = po.histogram(img, bits)

### WYLICZ ENTROPIE 
print(po.entropy(img_hist))
