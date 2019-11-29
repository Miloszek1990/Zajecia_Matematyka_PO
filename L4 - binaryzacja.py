#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:36:44 2019

@author: foton
"""
import matplotlib.pyplot as plt

import polib as po

### Binaryzacja obrazów
#
# 1. Stwórz funkcje kontrolującą wielkości jądra filtrującego
# 1.1 Funkcja przyjmuje jako argument obraz/wielkość obrazu i rozmiar jądra filtrującego
# 1.2 Funkcja sprawdza nieparzystość wielkości jądra
# 1.3 Funkcja sprawdza czy jądro nie jest większe od obrazu
# 1.4 Funkcja zwraca połowe wielkości jądra
#
# 2. Stwórz funkcje binaryzującą obraz bezkontekstowo względem progu
# 2.1 Funkcja przyjmuje obraz i threshold
# 
# 3. Stwórz funkcje binaryzującą obraz kontekstowo
# 3.1 Funkcja przyjmuje obraz i wielkość jądra
# 3.2 Wewnętrznie wywołuje funkcje obliczającą połowe wielkości jądra
# 3.3 Pętle iterują po obrazie ale bez krawędzi o wielkości połowy wielkości jądra 
try:
    bits = 8
    image_path = "../tekst.png"
    img = po.read_image_matplotlib(image_path, bits, 0)
    img_info = (img.shape[0], img.shape[1], bits)
    
    #img_binarized = po.thr_norm(img, 5, img_info)
    img_binarized = po.thr_adapt(img, 3, img_info)
    
    max_val = (2**bits - 1)
    plt.imshow(img_binarized, 
               cmap = "gray", 
               vmin = 0, 
               vmax = max_val)
    plt.imsave("L4 - text_binarized_global_adaptive.png", 
               img_binarized,
               cmap = "gray",
               vmin = 0, 
               vmax = max_val)
except Exception as ex:
    print("Some error: ")
    print(ex)
    










