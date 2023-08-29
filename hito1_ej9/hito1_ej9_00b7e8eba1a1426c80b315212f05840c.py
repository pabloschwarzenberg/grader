#Sistema de Ecuaciones
print("Digite los valores de a,b,c,d,e,f")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
determine = a*e - b*d
if determine != 0:
   x = (c*e - b*f) / determine
   y = (a*f - c*d) / determine    
print("x = ",x, "y = ",y)
