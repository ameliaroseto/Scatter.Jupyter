
**Author:** **Amelia Roseto**

## Specification

Consider the following set of coupled first-order ODEs for three real-valued functions of time x(t), y(t), z(t), with real-valued constants a, b, c, and initial conditions at 

                          t = 0: x ̇ = −y − z,  y ̇ = x + a y, z ̇ = b + z(x − c), x(0) = y(0) = z(0) = 0


Recall that the over-dot notation is Newton’s short-hand for a time derivative, e.g., x ̇ ≡ dx/dt. For our purposes, we will set a = b = 0.2 and leave c as a tunable parameter. Note that this system of equations has only a single nonlinear term zx in the z ̇ equation. This nonlinearity makes the system impossible to solve analytically, but also leads to very interesting behavior that you will explore numerically in this final.


# Problem 1
In final.py, write a python function solve odes(c, T=500, dt=0.001) that inte- grates the Eqs. (1), given the tunable parameter c, the final time T , and the time step dt. The function should return a pandas dataframe of four numpy arrays of float64 values: pd.DataFrame("t":t, "x":x, "y":y, "z":z). The array t should store time points in the domain [0,T] with equal spacing dt. The arrays x, y, and z should be pre-allocated as arrays of zeros for efficiency. A single for loop should then integrate Eqs. (1) using the 4th-order Runge-Kutta method from the initial conditions x = y = z = 0 at t = 0 over the array of t values and store the results in the corresponding arrays. Write at least one test function to check your implementation.

# Problem 2
In final.py, write seven plotting functions that use matplotlib to visualize the solu- tion: three time plots plotx(sol) (x vs t, 2pt), ploty(sol) (y vs t, 2pt), plotz(sol) (z vs t, 2pt), three 2D plots plotxy(sol, S=100) (y vs x, 2pt), plotyz(sol, S=100) (z vs y, 2pt), plotxz(sol, S=100) (z vs x, 2pt), and one 3D plot plotxyz(sol, S=100) (z vs x-y, 3pt). In each function, assume that sol is the DataFrame output by solve odes. The time plots should show the domain t ∈ [0, T ], while the 2D and 3D plots should include only the steady-state time domain t ∈ [S,T] that discards transient behavior. (Hint: there are N = ⌊S/dt⌋ points to discard.) Plots should be labeled clearly, with x and y having fixed range [−12, 12], and z having fixed range [0, 25]. Demonstrate all functionality in Final.ipynb using c = 2.

# Problem 3
Explore the onset of chaotic behavior. In your notebook, show a time plot x(t), a 2D plot y(x), and a 3D plot z(x,y) for each of the following c values: 3, 4, 4.15, 4.2, and 5.7. Show other plots as desired. In your notebook, describe in detail what is happening in each case.

# Problem 4
Examine structure of the local maxima. Create a function findmaxima(x, S=100) that isolates local maxima of a particular solution array x, after discarding the first S points (to ignore transient behavior), and returns a numpy array of the local maxima: xmax. Create a function scatter(dc=0.01) that for each value c in the range [2, 6] with a small mesh spacing dc solves Eqs. (1) and extracts the set of maximal points of x, then plots each maximal point (c, x) on the same scatter plot of x vs c. After plotting all such points, you will have a graph of (the multi-valued function of) the asymptotic local maxima of x vs c. The range of x in the plot should be from [3,12]. Comment on your findings.



## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Amelia Roseto**
