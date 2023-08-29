#Sistema de Ecuaciones
from scipy.optimize import fsolve
from math import sin,cos
 
def solve_function(unsolved_value):
    x=unsolved_value[0]
    return [
        sin(x)-0.5
    ]
 
solved=fsolve(solve_function,[3.14])
print(solved)
solved=fsolve(solve_function,[0])
print(solved)
 
print("Program done!")