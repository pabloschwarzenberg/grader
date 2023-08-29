#Sistema de Ecuaciones 
from sympy 
eq1 = Eq((x+y), 1) 
print("Equation 1:") 
print(eq1) 
eq2 = Eq((x-y), 1) 
print("Equation 2") 
print(eq2) 
  
print("Values of 2 unknown variable are as follows:") 
  
print(solve((eq1, eq2),(x, y))) 