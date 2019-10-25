#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:13:43 2019

@author: foton
"""

### Podstawowe biblioteki
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

### OpenCV
# Wczytanie obrazu
img = cv2.imread("./Lenna.png", cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR -> flag==1
img = cv2.imread("./Lenna.png", cv2.IMREAD_GRAYSCALE) # cv2.IMREAD_GRAYSCALE -> flag==0

cv2.imshow("norm_image", img)# Wyświetlenie obrazu
cv2.imwrite("nazwa.png", img)# Zapisanie obrazu

### Numpy
# Input data
N_points      = 1000
phase         = 0#np.pi/7
N_waves       = 2
amplitude_mul = 2
amplitude_add = 0

# Make data
X_data = np.linspace(0, N_points-1, N_points) # Tworzenie wektora/tablicy liczb (OD, DO, ILE) 
X_data = X_data.astype(int) # Zamiana typu wartości stworzonego obiektu

Y_data = amplitude_mul * np.sin( N_waves * (2 * np.pi)/N_points * X_data + phase) + amplitude_add # Stworzenie wektora sinus od 0 do 2*pi z ilościa punktów N_pts
Y_data = Y_data + np.max(Y_data) # Przesuń do góry aby mieć tylko wartości nieujemne

Y_mtx = [Y_data for _ in range(N_points)]
Y_mtx = np.array(Y_mtx)

Y_mtx = cv2.normalize(Y_mtx, 
                      None, 
                      alpha = 0, 
                      beta = 255, 
                      norm_type = cv2.NORM_MINMAX, 
                      dtype = cv2.CV_8UC1) # Znormalizuj dane do 8 bitowego obrazu

cv2.imshow("norm_image", Y_mtx)
cv2.imwrite("Z1-sin_img.png", Y_mtx)

### Matplotlib
# Wyświetl dane
plt.plot(X_data, 
         Y_data,
         marker = "o",
         color = "m",
         linestyle = ":")
plt.xlabel("x [-]")
plt.ylabel(r"Wave function $Y\left(x\right) = A\cdot\sin\left( \frac{2\pi}{x}+\theta\right) + \Phi + \max\left(Y\left(x\right)\right)$")
plt.show()
plt.tight_layout()
plt.show()
plt.savefig("Z1-some_plot.png", dpi=300)

# Trochę bardziej zaawansowanie
fig, (ax1,ax2) = plt.subplots(1,2)

ax1.plot(X_data, Y_data)
ax1.set_xlabel("x [-]")
ax1.set_ylabel(r"Wave function $Y\left(x\right) = A\cdot\sin\left( \frac{2\pi}{x}+\theta\right) + \Phi + \max\left(Y\left(x\right)\right)$")

ax2.plot(X_data, X_data)
ax2.set_xlabel("x [-]")
ax2.set_ylabel("x [-]")

fig.tight_layout()
fig.show()
fig.savefig("Z1-some_plot.png", dpi=300)

# W przypadku braku biblioteki OpenCV można wczytać 8-bitowy obraz w postaci
# obiektu Numpy macierzy za pomocą matplotliba i Numpy
import matplotlib.image as mpimg

img = mpimg.imread('./Lenna.png')
img_R = np.matrix((img[:,:,0] * 255)).astype(int)
img_G = np.matrix((img[:,:,1] * 255)).astype(int)
img_B = np.matrix((img[:,:,2] * 255)).astype(int)

plt.imshow(img)
plt.imsave("Lenna_new.png", img)
     























