#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import numba as nb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

@nb.jit
def dxdt(x, y, z):
    "define x dot as -y-z"
    dx = -y - z
    return dx

@nb.jit
def dydt(x, y, z, a):
    "define y dot as x+ay"
    dy = x + a*(y)
    return dy

@nb.jit
def dzdt(x, y, z, b, c):
    "define z dot as b + z(x-c)"
    dz = b + z*(x-c)
    return dz

@nb.jit
def solve_odes(c, T = 500, dt = 0.001, a = 0.2, b = 0.2):
    """ c = tunable parameter, T = final time, dt = time step
arrays x, y, and z should be pre set as an array of zeros
z = 0, y = 0, x = 0 => @ t = 0"""
    t = np.arange(0, T, dt)
    x = np.zeros_like(t)
    x[0] = 0
    y = np.zeros_like(t)
    y[0] = 0
    z = np.zeros_like(t)
    z[0] = 0

    for i in range (0,len(t)-1):

        k1x = dt*dxdt(x[i], y[i], z[i])
        k1y = dt*dydt(x[i], y[i], z[i], a)
        k1z = dt*dzdt(x[i], y[i], z[i], b, c)

        k2x = dt*dxdt(x[i]+k1x/2, y[i]+k1y/2, z[i]+k1z/2)
        k2y = dt*dydt(x[i]+k1x/2, y[i]+k1y/2, z[i]+k1z/2, a)
        k2z = dt*dzdt(x[i]+k1x/2, y[i]+k1y/2, z[i]+k1z/2, b, c)

        k3x = dt*dxdt(x[i]+k2x/2, y[i]+k2y/2, z[i]+k2z/2)
        k3y = dt*dydt(x[i]+k2x/2, y[i]+k2y/2, z[i]+k2z/2, a)
        k3z = dt*dzdt(x[i]+k2x/2, y[i]+k2y/2, z[i]+k2z/2, b, c)

        k4x = dt*dxdt(x[i]+k3x, y[i]+k3y, z[i]+k3z)
        k4y = dt*dydt(x[i]+k3x, y[i]+k3y, z[i]+k3z, a)
        k4z = dt*dzdt(x[i]+k3x, y[i]+k3y, z[i]+k3z, b, c)
        x[i+1]= x[i]+(k1x+2*k2x+2*k3x+k4x)/6
        y[i+1]= y[i]+(k1y+2*k2y+2*k3y+k4y)/6
        z[i+1]= z[i]+(k1z+2*k2z+2*k3z+k4z)/6
    return pd.DataFrame({"t":t, "x":x, "y":y, "z":z})

def plotx(sol):
    """"this plots the x vs t time plot!"""
    with plt.xkcd():
        plt.figure()
        t = sol['t']
        x = sol['x']
        plt.plot(t, x,color="pink",label='x vs t')
        plt.legend(loc='upper left')
        plt.xlabel('T')
        plt.ylabel('X')
        plt.title('Plot of x vs t')
        plt.ylim((-12,12))

def ploty(sol):
    """"this plots the y vs t time plot!"""
    with plt.xkcd():
        plt.figure()
        t = sol['t']
        y = sol['y']
        plt.plot(t, y,color="pink",label='y vs t')
        plt.legend(loc='upper left')
        plt.xlabel('T')
        plt.ylabel('Y')
        plt.title('Plot of y vs t')
        plt.ylim((-12,12))

def plotz(sol):
    """"this plots the z vs t time plot!"""
    with plt.xkcd():
        plt.figure()
        t = sol['t']
        z = sol['z']
        plt.plot(t, z,color="pink",label='z vs t')
        plt.legend(loc='upper left')
        plt.xlabel('T')
        plt.ylabel('Z')
        plt.title('Plot of z vs t')
        plt.ylim((-12,12))

def plotxy(sol, S = 100, T=500):
    """"this plots the x vs y 2D plot!"""
    with plt.xkcd():
        plt.figure()
        dt = .001
        N = int(S/dt)
        x = sol['x'][N:]
        y = sol['y'][N:]
        plt.plot(x, y,color= "m",label='x vs y')
        plt.legend(loc='upper left')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Plot of x vs y')
        plt.ylim((-12,12))
        plt.xlim((-12,12))

def plotzy(sol, S = 100, T=500):
    """"this plots the z vs y 2D plot!"""
    with plt.xkcd():
        plt.figure()
        dt = .001
        N = int(S/dt)
        z = sol['z'][N:]
        y = sol['y'][N:]
        plt.plot(z, y,color="m",label='z vs y')
        plt.legend(loc='upper left')
        plt.xlabel('Z')
        plt.ylabel('Y')
        plt.title('Plot of z vs y')
        plt.ylim((-12,12))
        plt.xlim((-12,12))

def plotzx(sol, S = 100, T=500):
    """"this plots the x vs z 2D plot!"""
    with plt.xkcd():
        plt.figure()
        dt = .001
        N = int(S/dt)
        x = sol['x'][N:]
        z = sol['z'][N:]
        plt.plot(x, z,color="m",label='z vs x')
        plt.legend(loc='upper left')
        plt.xlabel('X')
        plt.ylabel('Z')
        plt.title('Plot of z vs x')
        plt.ylim((-12,12))
        plt.xlim((-12,12))

def plotxyz(sol, S = 100, T=500):
    with plt.xkcd():
        plt.figure()
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        """"this plots the z vs y-x 2D plot!"""
        x = sol['x']
        y = sol['y']
        z = sol['z']
        plt.plot(x, y, z,color="c",label='z vs y-x')
        plt.legend(loc='upper left')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Plot of z vs y-x')
        plt.ylim((-12,12))
        plt.xlim((-12,12))

@nb.jit
def findmaxima(sol, S=100):
    """for i in range __ if i is greater than i-1 and i+1 add i to list to #collect all maximums, same for minimum but opposite"""
    x = sol['x'][S:]
    tmax = []
    xmax = []
    i = 0
    for i in range(S+1, S+len(x) -1):
        if x[i]>x[i-1] and x[i]>x[i+1]:
            xmax.append(x[i])
    return (xmax)

def scatter(xmax, dc = 0.01, dt=1):
    """for each value of c in range [2,6] with the spacing of dc"""
    ds = np.arange(2, 6, dc)
    for c in ds:
        sol = solve_odes(c, T = 500, dt = .001, a = 0.2, b = 0.2)
        xmax =findmaxima(sol, S=100)
        plt.scatter((c*np.ones_like(xmax)), xmax, marker = ".", color = "purple")
    plt.xlabel("c")
    plt.ylabel("x")
    plt.show()
