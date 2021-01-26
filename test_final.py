#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import final as fn

def test_final():
    """check if the last values are correct"""
    assert np.solve_odes(-0.9, 0, np.arange(0, 2*np.pi*50, 0.001), 0.18)[-1] < -0.816
    assert np.solve_odes(-0.9, 0, np.arange(0, 2*np.pi*50, 0.001), 0.18)[-1] > -0.816    
    print("Nice work, good effort!")
