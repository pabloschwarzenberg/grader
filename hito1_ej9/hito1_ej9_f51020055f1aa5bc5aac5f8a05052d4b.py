#Sistema de Ecuaciones
 #Sistema de Ecuaciones
a = int(input("Ingrese a: "))     
b = int(input("Ingrese b: "))     
c = int(input("Ingrese c: "))     
d = int(input("Ingrese d: "))     
e = int(input("Ingrese e: "))     
f = int(input("Ingrese f: "))     
 
determinante = a*e-b*d
 
if determinante !=0:
     x = (c*e - b*f) /determinante
     y = (a*f - c*d) /determinante
     print("x="+str(x))
     print("y="+str(y)) 
     
else:
   print("x=0")
   print("y=0")     