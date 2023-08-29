#Aprobación de créditos
ingreso = int(input("ingrese sus ingresos en pesos: "))
naciemiento = int(input("ingrese su año de naciemiento: "))
hijos = int(input("ingrese su numero de hijos: "))
pertenencia = int(input("ingrese sus años de pertenencia en el banco: "))
Ecivil = str(input("ingrese su estado civil soltero,""S"" o casado,""C"": "))
vive = str(input("ingrese si vive en campo,""R"" o en ciudad,""U"": "))

C = casado
S = soltero

if pertenencia > 10 and hijos >= 2:
  print("APROBADO")
elif Ecivil == Casado and hijos >= 3 and 45 <= nacimiento <= 55:
  print("APROBADO")