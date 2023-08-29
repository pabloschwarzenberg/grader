ingreso = int(input("Ingrese sus ingresos anuales en pesos: "))
anio = int(input("Año: "))
hijos = int(input("¿Cuantos hijos tiene? "))
pertenencia = int(input("¿Cuantos años lleva perteneciendo al banco? "))
edad = 2022 - anio
print("Estado civil\nIngrese su estado civil de la siguiente forma")
est = input("S: Soltero, C: Casado")

print("Vive en cammpo o ciudad?")
CoC = input("U: urbano, R: rural")

if (anio>=10 and hijos >=2):
  print("APROBADO")
elif (est == "C" and hijos>=3 and 44<edad<56):
  print("APROBADO")
elif (ingreso>=2500000 and est=="S" and CoC == "U"):
  print("APROBADO")
elif (ingreso>=3500000 and pertenencia>= 5):
  print("APROBADO")
elif (CoC == "R" and est== "C" and hijos<=2):
  print ("APROBADO")
else:
  print("RECHAZADO")