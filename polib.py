#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:07:36 2019

@author: foton
"""
import sys
import random

import numpy as np
import matplotlib.image as mpimg

###
### HELP FUNCTIONS
###
#
# "public"
#
def read_image_matplotlib(image_path, bits, layer=0):
    # read image by matplotlib library
    
    img = mpimg.imread(image_path)
    img = np.matrix((img[:,:,layer]) * (2**bits - 1)).astype(int)

    return img

def noise_image(img_size, bits):
    # generate white noise image
    
    noise = np.zeros(img_size)
    for row in range(img_size[0]):
        for col in range(img_size[1]):
            noise[row, col] = random.randint(0, (2**bits-1))
    
    return noise
    
###
### CONTROL FUNCTIONS
###
#
# "public"
#
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
#
# "public"
#
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

def entropy(hist_dict):
    # Calculate entropy
    
    hist_vals_arr = np.array(list(hist_dict.values()))+1
    hist_vals_arr = hist_vals_arr/np.sum(np.sum(hist_vals_arr))
    entr = -np.sum(hist_vals_arr*np.log2(hist_vals_arr))

    return entr

###
### FILTERING FUNCTIONS 
###
#
# "private"
#
def check_threshold_value(threshold, max_px_val):
    
    if threshold > max_px_val:
        threshold = max_px_val
    elif threshold < 0:
        threshold = 0
    
    return threshold

def threshold_the_px(px_val, threshold, max_px_val):
    
    if px_val >= threshold:
        px_val = max_px_val
    elif px_val < threshold:
        px_val = 0
    
    return px_val
    
#
# "public"
#
### NONCONTEXT
def thr_norm(img, thr, img_info):
    # Normal threshold
    
    max_px_value = 2**img_info[2]
    img_copy = img.copy()
    
    for i in range(img_info[0]):
        for j in range(img_info[1]):
            
            img_copy[i,j] = threshold_the_px(img_copy[i,j] , thr, max_px_value)
    
    return img_copy

### CONTEXT - CONVOLUTIONAL
def thr_adapt(img, kernel_size, img_info, C=0):
    # Adaptive threshold
    
    max_px_value = 2**img_info[2]
    img_copy = img.copy()
    h_KS = half_kernel_size(img, kernel_size)
    
    for i in range(h_KS, img_info[0] - h_KS):
        for j in range(h_KS, img_info[1] - h_KS):
            
            mask = np.ones([kernel_size, kernel_size])           
            for k in range(kernel_size):
                for m in range(kernel_size):
                    i_tmp_mask = i + h_KS - k
                    j_tmp_mask = j + h_KS - m
                    mask[k,m] = img[i_tmp_mask, j_tmp_mask] 
            
            thr = int(np.mean(mask)) + C
            thr = check_threshold_value(thr, max_px_value)
            
            img_copy[i,j] = threshold_the_px(img_copy[i,j] , thr, max_px_value)

    return img_copy