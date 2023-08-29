#Aprobación de créditos

ingresos = int(input("Ingrese su ingreso:  $"))
añonacimiento = int(input("Ingrese año de nacimiento:  "))
n_hijos = int(input("Ingrese numero de hijos:  "))
añosbanco = int(input("Ingrese años perteneciente al banco:  "))
estadocivil = input("Ingrese estado civil (S: Soltero, C: Casado):  ")
vivienda = input("¿Vive en zona urbana ( U ) o rural ( R )?:  ")
edad = (2023 - añonacimiento)

print(edad)

if ( añosbanco >= 10 and n_hijos >= 2 ):
  print("APROBADO")

elif ( estadocivil == "C" and n_hijos >= 3 and edad >= 45 and edad <= 55):
  print("APROBADO")

elif ( ingresos > 2500000 and estadocivil == "S" and vivienda == "C"):
  print("APROBADO")

elif ( ingresos > 3500000 and añosbanco >= 5 ):
  print("APROBANDO")

elif ( vivienda == "R" and estadocivil == "C" and n_hijos <= 2 ):
  print("APROBADO")      