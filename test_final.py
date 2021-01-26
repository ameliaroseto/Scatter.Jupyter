#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Amelia Roseto
#Student ID: 2289652
#Email: roseto@chapman.edu
#Course: PHYS220/MATH220/CPSC220 Fall 2018
#Assignment: FINAL BABY!!!!!
###

import matplotlib.pyplot as plt
import numpy as np
import final as fn

def test_final():
    """check if the last values are correct"""
    assert np.solve_odes(-0.9, 0, np.arange(0, 2*np.pi*50, 0.001), 0.18)[-1] < -0.816
    assert np.solve_odes(-0.9, 0, np.arange(0, 2*np.pi*50, 0.001), 0.18)[-1] > -0.816    
    print("Nice work, good effort!")
