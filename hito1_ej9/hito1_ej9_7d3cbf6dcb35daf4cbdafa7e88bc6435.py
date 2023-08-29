#Sistema de Ecuaciones
print('Rellene los ponderadores según corresponda\n\nax + by = c \ndx + ey = f\n')
a = float(input("a:  "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))
print('\n')
print(a,'x', '+' , b,'y' , '=' , c)
print(d,'x', '+' , e,'y' , '=' , f)
print('\n')
if (b*d - a*e)==0:
  print('Math Error')

else:
  y = (c*d - a*f)/(b*d - a*e)
  x = (c - b*y)/a
  print('x = ', x)
  print('y = ', y)
