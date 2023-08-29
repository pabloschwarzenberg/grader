#Sistema de Ecuaciones
print("Sistema De Ecuaciones 2x2 De La Forma: A*x+B*y=C D*x+E*y=F")
import math
a = eval(input("Valor A:"))
b = eval(input("Valor B:"))
c = eval(input("Valor C:"))
d = eval(input("Valor D:"))
e = eval(input("Valor E:"))
f = eval(input("Valor F:"))

Det = a*e-d*b
Detx = c*e-b*f
Dety = a*f-d*c

if Det==0:
    print("No Existe Solución Única Para El Sistema")

else:    
    x = Detx/Det
    y = Dety/Det
    print("x = ",x)
    print("y = ",y)
