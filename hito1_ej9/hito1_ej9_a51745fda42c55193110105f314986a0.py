#Sistema de Ecuaciones
a = float(input("Ingrese a "))
b = float(input("Ingrese b "))
c = float(input("Ingrese c "))
d = float(input("Ingrese d "))
e = float(input("Ingrese e "))
f = float(input("Ingrese f "))

det = a * e - b * d

if det != 0 :
   x = float((e * c - b * f) / det)
   y = float((a * f - d * c) / det)

   print("x="+str(x))
   print("y="+str(y))