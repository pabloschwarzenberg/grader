ingresos=int(input("ingresos"))
añodenacimiento=int(input("Año de nacimiento"))
edad=2023-añodenacimiento
hijos=int(input("Ingrese el numero de hijos"))
pertenecia=int(input("Años en el banco"))
print("Estadi civil: Soltero: s; casado: c")
civil=input("Ingrese estado civil")
print("Rural: r; Urbano: u ")
vivienda=input("Ingrese su vivienda")
if pertenecia > 10 and hijos >= 2:
  print("APROBADO")
elif civil == "C" and hijos > 3 and edad >= 45 and edad <= 55:
  print("APROBADO")
elif ingresos > 2500000 and civil == "S" and vivienda == "U":
  print("APROBADO")
elif ingresos > 3500000 and pertenecia >= 5:
  print("APROBADO")
elif vivienda == "R" and civil == "C" and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")