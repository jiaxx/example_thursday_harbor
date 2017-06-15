# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:10:36 2017

@author: Xiaoxuan Jia
"""
import numpy as np

def snr(W):
    """Calculate snr of sorted units based on Xiaoxuan's matlab code. 
    Signal to noise ratio for waveform shape.
    W: (waveforms from all spike times), first dim is rep
    ref: (Nordhausen et al., 1996; Suner et al., 2005)
    """
    W_bar = np.nanmean(W,axis=0)
    A = max(W_bar) - min(W_bar)
    e = W - np.tile(W_bar,(np.shape(W)[0],1))
    snr = A/(2*np.nanstd(e.flatten()))
    
    return snr      
