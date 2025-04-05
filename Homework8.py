import scipy as s
import numpy as np

x = [-31, -5, 1, 11, 61]
y = [-2, -1, 1, 2, 3]

poly = s.interpolate.lagrange(x,y)
print("Lagrange: ", poly(0))


cs = s.interpolate.CubicSpline(x,y, bc_type = 'natural')
print("Cubic Spline: ", cs(0))

