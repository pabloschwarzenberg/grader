#Aprobación de créditos
 Ingreso = int(input("Ingrese su monto en pesos:"))

AñoNacimiento = int(input("Ingrese su año de nacimiento:"))

NumeroHijos = int(input("Ingrese cantidad de hijos:"))

AñosEnBanco = int(input("Ingrese años de pertenencia al banco]:"))

Estado = str(input("Ingrese si es Soltero (S) o casado (C):"))

CampoOCiudad = str(input("Ingrese si vive en campo (R) o ciudad (U):"))



AñoActual = 2022

Edad = AñoActual - AñoNacimiento



if AñosEnBanco > 10 and NumeroHijos >= 2:

  print("APROBADO")



if str(Estado) == "C" and NumeroHijos > 3 and Edad > 45 and Edad < 55:


print("APROBADO")



if Ingreso > 2500000 and str(Estado) == "S" and str(CampoOCiudad) == "U":

  print("APROBADO")



if Ingreso > 3500000 and AñosEnBanco > 5:

  print("APROBADO")



if str(CampoOCiudad) == "R" and str(Estado) == "C" and NumeroHijos < 2:

  print("APROBADO")   

16:45
a1 = float(input("a1 = "))

b1 = float(input("b1 = "))

c1 = float(input("c1 = "))

a2 = float(input("a2 = "))

b2 = float(input("b2 = "))

c2 = float(input("c2 = "))

if a1/a2==b1/b2 and b1/b2==c1/c2:

  print("Infinitas soluciones")

elif a1/a2==b1/b2 and b1/b2!=c1/c2:

  print("No tiene solución")

else:

  x=(c1*b2-c2*b1)/(a1*b2-a2*b1)

  y=(a1*c2-a2*c1)/(a1*b2-a2*b1)

  print("x=", round(x,1))

  print("y=", round(y,1))   