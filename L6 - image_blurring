#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:21:38 2018

@author: foton
"""
import numpy as np
import polib as po

# Ścieżka do obrazu
img_path = "./ciemna_strona_ksiezyca_brud.png"

# wczytaj obraz
#img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img = po.read_image_matplotlib(img_path, 8)

# metoda filtracji
#["mean", "median", "gauss"]
filtration = "median" 

# wielkośc jądra filtrującego
kernel_size = [3, 5, 7]

imgs = []
for k in kernel_size:
    # sprawdz porawność rozmiaru jądra
    img_copy = img.copy()
    h_KS = po.half_kernel_size(img, k)
    
    if filtration  == "mean":
        img_blured = po.blur_method_mean(img_copy, k)
    elif filtration == "median":
        img_blured = po.blur_method_median(img_copy, k)

    imgs.append(img_blured)

stacked_img = np.hstack(imgs)

po.show_image_by_pyplot(stacked_img, 8)
po.save_image_by_pyplot(stacked_img, 8, "median_filter_3-5-7.png")