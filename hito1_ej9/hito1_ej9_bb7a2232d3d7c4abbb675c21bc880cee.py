#Sistema de Ecuaciones
x=-3.0
y=4.0

%matplotlib inline 

import matplotlib.pyplot as plt
import sympy 
import numpy as np 
from scipy import integrate 

x = sympy.Symbol('x')
y = sympy.Function('y')

a=-5
b=-1
c=4
d=-1

    def ODE(a,b,c,t):

        f = a*x+b*y
        g = c*x+c*d
         init_printing(use_unicode=True)
             return f,g




sympy.Eq(x(x).diff(t), f)
sympy.Eq(y(x).diff(t), g)