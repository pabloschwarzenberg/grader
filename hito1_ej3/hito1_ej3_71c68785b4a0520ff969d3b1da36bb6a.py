#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso en pesos: "))
anacimiento = int(input("Ingrese su año de nacimiento: "))
nuhijos = int(input("Ingrese el número de hijos: "))
apertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado= input("Ingrese su estado civil (S para soltero, C para casado): ")
ubi = input("Ingrese su ubicación (U para urbano, R para rural): ")

aprobado = False

if apertenencia > 10 and nuhijos >= 2:
    aprobado = True

elif estado == "C" and nuhijos > 3 and 45 <= (2023 - anacimiento) <= 55:
    aprobado = True

elif ingreso > 2500000 and estado == "S" and ubi == "U":
    aprobado = True

elif ingreso > 3500000 and apertenencia > 5:
    aprobado = True

elif ubi == "R" and estado == "C" and nuhijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
  print("RECHAZADO")