#Sistema de Ecuaciones
a = float(input("ingrese el primer coeficiente "))   
b = float(input("ingrese el segundo coeficiente "))   
c = float(input("ingrese el tercer coeficiente "))   
d = float(input("ingrese el cuarto coeficiente "))   
e = float(input("ingrese el quinto coeficiente "))   
f = float(input("ingrese el sexto coeficiente "))

det = float(a*e - b*d)

if det != 0:
  x = round(float((e*c - b*f)/det),1)
  y = round(float((a*f - d*c)/det),1)
  print("[x=%s,y=%s]" %(x,y))
  
else:
     m = d/a
     if m * c == f:
          print("el sistema posee infinitas soluciones")
     else:
          print("este sistema no posee solucion")