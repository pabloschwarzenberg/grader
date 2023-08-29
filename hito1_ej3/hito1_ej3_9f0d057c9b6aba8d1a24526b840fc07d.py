#Aprobación de créditos
ingresos = int(input(" ingrese su ingreso: "))
fechaNacimiento = int(input(" ingrese su año de nacimiento: "))
hijos = int(input(" ingrese su numero de hijos: "))
pertenencia = int(input(" ingrese sus años de pertenencia en el banco: "))
estadoCivil = input(" ingrese su estado civil: ")
vivienda = input(" ingrese donde vive: ")
#calculo edad
edad = (2020 - fechaNacimiento)
#salida
if pertenencia > 10 and hijos >= 2:
  print("APROBADO")
elif estadoCivil == "C" and hijos > 3 and 45<=edad<=55:
     print("APROBADO")
elif ingresos > 2500000 and estadoCivil == "S" and vivienda == "U":
    print("APROBADO")
elif ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estadoCivil == "C" and hijos < 2:
    print("APROBADO")
else: 
    print("RECHAZADO")