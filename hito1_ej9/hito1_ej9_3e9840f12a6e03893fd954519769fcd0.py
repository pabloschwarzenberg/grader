#Sistema de Ecuaciones
print('Inserte primera ecuacion',"\n") 
a = float(input('Inserte su X:')) 
b = float(input('Inserte su Y:')) 
c = float(input('Inserte su numero:')) 
 
print('\nsegunda ecuacion') 
A = float(input('Inserte su X:')) 
B = float(input('Inserte su Y:')) 
C = float(input('Inserte su numero:')) 
 
 
 
if (a*B) != (A*b): 
    x=((c*B)-(b*C))/((a*B)-(b*A)) 
    y=((a*C)-(c*A))/((a*B)-(b*A)) 
    print('x = %4.2f' %x) 
    print('y = %4.2f' %y) 
else: 
    print('Ecuacion incompatible') 
