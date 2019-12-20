#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:07:36 2019

@author: foton
"""
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sys

###
### HELP FUNCTIONS
###
def read_image_matplotlib(image_path, bits):
    # read image by matplotlib library
    
    img = mpimg.imread(image_path)
    img = np.matrix((img[:,:,0]) * (2**bits - 1)).astype(int)

    return img

def show_image_by_pyplot(img, bits):
    max_val = (2**bits - 1)
    plt.imshow(img, 
               cmap = "gray", 
               vmin = 0, 
               vmax = max_val)

def save_image_by_pyplot(img, bits, name):
    max_val = (2**bits - 1)
    plt.imsave(name, 
               img,
               cmap = "gray",
               vmin = 0, 
               vmax = max_val)
###
### CONTROL FUNCTIONS
###
def half_kernel_size(img, KS):
    ### SPRAWDZANIE ROZMIARU JĄDRA
    # przy jakimkolwiek błędzie, zmieniony zostanie na 1
    # wartość 1 wywoła wyłącznie programu po sprawdzeniu wszystkich możliwości
    exit_status = 0 
    
    # 1. Sprawdz czy rozmiar jądra jest liczbą nieparzystą
    if KS % 2 == 0:
        print("Jądro musi być liczbą nieparzystą.\n")
        exit_status = 1
    
    h_KS = int(KS/2) # dobrze, że tylko srodkowy element minus 1    
    # 2. Sprawdz czy rozmiar jądra jest liczbą mniejszą niż połowa którego kolwiek rozmiaru obrazu
    if KS > int(img.shape[0]/2):
        print("Rozmiar połowy obrazu w X to: " + str(img.shape[0]/2))
        print("Rozmiar symetrycznego jądra to: " + str(KS))
        print("Rozmiar jądra nie może być większy niż: " + str(h_KS) + "\n")
        exit_status = 1
    if KS > int(img.shape[1]/2):
        print("Rozmiar połowy obrazu w Y to: "+ str(img.shape[1]/2))
        print("Rozmiar symetrycznego jądra to: " + str(KS))
        print("Rozmiar jądra nie może być większy niż: " + str(h_KS) + "\n")
        exit_status = 1
    
    if exit_status == 1:
        sys.exit()
    
    return h_KS

###
### ANALYSE FUNCTION
###
def histogram(mtx, bits=8, normalize=False):
    # Calculate histogram of image
    histogram = {i:0 for i in range(2**bits)}
    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            histogram[mtx[i,j]] += 1
    
    if normalize == True:
        mtx_size = mtx.shape[0] * mtx.shape[1]
        for i in range(2**bits):
            histogram[i] = histogram[i] / mtx_size
    
    return histogram

def entropia(hist_dict):
    # Calculate entropy
    
    hist_vals_arr = np.array(list(hist_dict.values()))+1
    hist_vals_arr = hist_vals_arr/np.sum(np.sum(hist_vals_arr))
    entr = -np.sum(hist_vals_arr*np.log2(hist_vals_arr))

    return entr

###
### FILTERING FUNCTIONS 
###
    
### NONCONTEXT
def thr_norm(img, thr):
    # Normal threshold
    
    rows = img.shape[0]
    cols = img.shape[1]
    img_copy = img.copy()
    
    for i in range(rows):
        for j in range(cols):
            
            if img_copy[i,j] >= thr:
                img_copy[i,j] = 255
            elif img_copy[i,j] < thr:
                img_copy[i,j] = 0
    
    return img_copy

### CONTEXT - CONVOLUTIONAL
def thr_adapt(img, kernel_size, C=0):
    # Adaptive threshold
    
    rows = img.shape[0]
    cols = img.shape[1]
    img_copy = img.copy()
    h_KS = half_kernel_size(kernel_size)
    
    for i in range(h_KS, rows - h_KS):
        for j in range(h_KS, cols - h_KS):
            
            mask = np.ones([kernel_size, kernel_size])           
            for k in range(kernel_size):
                for m in range(kernel_size):
                    i_tmp_mask = i + h_KS - k
                    j_tmp_mask = j + h_KS - m
                    mask[k,m] = img[i_tmp_mask, j_tmp_mask] 
            
            thr = int(np.mean(mask)) + C
            #thr = int((np.max(mask)-np.min(mask))*0.5) + C
            #thr = int(np.median(mask)) + C
            
            if img_copy[i,j] >= thr:
                img_copy[i,j] = 255
            elif img_copy[i,j] < thr:
                img_copy[i,j] = 0

    return img_copy

def blur_method_mean(img, kernel_size):

    img_copy = img.copy() # troche kosztowne pamięciowo, ale spoko edukacjyjnie 

    h_KS = int(kernel_size/2)    
    for i in range(h_KS, img.shape[0] - h_KS):
        for j in range(h_KS, img.shape[1] - h_KS):
            
            mask = np.ones([kernel_size, kernel_size])
            k, m = 0, 0            
            for k in range(kernel_size):
                for m in range(kernel_size):
                    i_tmp_mask = i + h_KS - k
                    j_tmp_mask = j + h_KS - m
                    mask[k,m] = img[i_tmp_mask, j_tmp_mask] 
            
            img_copy[i,j] = np.mean(mask)
            
    return img_copy

def blur_method_median(img, kernel_size):

    img_copy = img.copy() # troche kosztowne pamięciowo, ale spoko edukacjyjnie 

    h_KS = int(kernel_size/2)    
    for i in range(h_KS, img.shape[0] - h_KS):
        for j in range(h_KS, img.shape[1] - h_KS):
            
            mask = np.ones([kernel_size, kernel_size])
            k, m = 0, 0            
            for k in range(kernel_size):
                for m in range(kernel_size):
                    i_tmp_mask = i + h_KS - k
                    j_tmp_mask = j + h_KS - m
                    mask[k,m] = img[i_tmp_mask, j_tmp_mask] 
            
            img_copy[i,j] = np.median(mask)

    return img_copy

def gaussian_kernel(half_kernel_size, sigma):
    
    norm = 1/(2*np.pi*sigma)
    down = 2*sigma**2
    
    GaussianBM = np.zeros( (half_kernel_size, half_kernel_size) ) # gaussian_blur_mask
    for i in range(0,half_kernel_size):
        for j in range(0,half_kernel_size):
            G_val = norm * np.exp(-((i-half_kernel_size)**2 + (j-half_kernel_size)**2)/down)
            
            GaussianBM[i,j] = G_val
    
    return GaussianBM

def gaussian_sigma_default(k):
    
    # Exaple visualization
    #sig_min = 3
    #sig_max = 27
    #sig_x = np.linspace(sig_min, sig_max, sig_max - sig_min + 1).astype(int)
    #sig_y = [sigma_default(x) for x in sig_x]
    #plt.bar(sig_x, sig_y)
    #plt.xlabel("Kernel size [-]")
    #plt.ylabel("Sigma default [-]")
    
    return 0.3 * ( ( (k-1) / 2)- 1) + 0.8


def blur_method_gaussian(img, mask):
    
    img_copy = img.copy() # troche kosztowne pamięciowo, ale spoko edukacjyjnie 

    kernel_size = mask.shape[0]
    h_KS = int(kernel_size/2)    
    for i in range(h_KS, img.shape[0] - h_KS):
        for j in range(h_KS, img.shape[1] - h_KS):
            
            mask_tmp = np.ones([kernel_size, kernel_size])     
            for k in range(kernel_size):
                for m in range(kernel_size):
                    i_tmp_mask = i + h_KS - k
                    j_tmp_mask = j + h_KS - m
                    mask_tmp[k,m] = img[i_tmp_mask, j_tmp_mask] * mask[k,m] 
            
            img_copy[i,j] = np.sum(mask_tmp)
    
    #img_copy = cv2.normalize(img_copy, img_copy, 0, 255, cv2.NORM_MINMAX)
    
    return img_copy

def edge_detection_by_mask(img, filtering_mask):
    
    img_edge = np.zeros( img.shape )
    
    for row in range(1, img.shape[0] - 1):
        for col in range(1, img.shape[1] - 1):
            
            mask00 = img[row - 1, col - 1] * filtering_mask[0, 0] #0
            mask01 = img[row - 1, col + 0] * filtering_mask[0, 1] #-1
            mask02 = img[row - 1, col + 1] * filtering_mask[0, 2] #0
            
            mask10 = img[row + 0, col - 1] * filtering_mask[1, 0] #-1
            mask11 = img[row + 0, col + 0] * filtering_mask[1, 1] #4
            mask12 = img[row + 0, col + 1] * filtering_mask[1, 2] #-1
            
            mask20 = img[row + 1, col - 1] * filtering_mask[2,0] #0
            mask21 = img[row + 1, col + 0] * filtering_mask[2,1] #-1
            mask22 = img[row + 1, col + 1] * filtering_mask[2,2] #0
    
            mask_sum = mask00 + mask01 + mask02 + mask10 + mask11 + mask12 + mask20 + mask21 + mask22
                       
            img_edge[row, col] = mask_sum
    
    return img_edge
