#Sistema de Ecuaciones
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

#Ahora resolveremos los sistemas

if a==d and b==e and c==f:
  print("El sistema tiene infinitas soluciones")
  
else:
 if (a*e==d*b) or ((a**2)*e==d*b):
   print("\nTu sistema de ecuaciones no tiene solución")

 else:
     y = round((d*c-a*f)/(d*b-a*e),1)
     x = round((f-e*y)/(d),1)
     print("\n¡Tus soluciones son:\nx=",x,"\ny=",y)
