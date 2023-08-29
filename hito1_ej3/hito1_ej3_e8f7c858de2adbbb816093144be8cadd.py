#Aprobación de créditos
ingreso = int(input("ingrese su ingreso en pesos: "))
año_nacimiento = int(input("ingrese su año de nacimiento: ")) 
hijos = int(input("ingrese la cantidad de hijos: "))
años_banco = int(input("ingrese la cantidad de años que lleva en el banco: "))
Estado_Civil = input("ingrese su estado civil (S: soltero, C, casado): ")
Vivienda = input("ingrese la ubicacion de su vivienda (U: urbano, R: rural): ")
edad = int(2022-año_nacimiento)
if años_banco > 10 and hijos >= 2:
  print("APROBADO")
elif Estado_Civil == "C" and hijos > 3 and edad > 45 and edad < 55:
  print("APROBADO")
elif ingreso > 2500000 and Estado_Civil == "S" and Vivienda == "U":
  print("APROBADO")
elif ingreso > 3500000 and años_banco > 5:
  print("APROBADO")
elif Vivienda == "R" and Estado_Civil == "C" and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")