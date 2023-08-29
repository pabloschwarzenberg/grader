#Aprobación de créditos
sueldo = int(input("ingrese su sueldo: "))
añoDeNaciomiento = int(input("ingrese su fecha de nacimiento: "))
edad = int(2021 - añoDeNaciomiento)
cantidadDeHijos = int(input("ingrese cantidad de hijos: "))
añosEnElBanco = int(input("¿cuantos años lleva perteneciendo a este banco?: "))
print("si esta casado debe poner una c y si esta soltero debe poner una s")
estadoCivil = input("ingrese su estado civil: ")
print("si usted vive en zona rural debe colocar una r y si vive en zona urbana debe colocar una u")
dondeVive = input("¿vive en zona rural o zona urbana?: ")

if añosEnElBanco >= 10 and cantidadDeHijos >= 2:
     print("APROBADO")

elif estadoCivil == "c" and cantidadDeHijos > 3 and edad <= 45 and edad >= 55:
     print("APROBADO")

elif sueldo > 2500000 and estadoCivil == "S" and dondeVive == "U":
     print("APROBADO")

elif sueldo > 3500000 and añosEnElBanco > 5:
     print("APROBADO")

elif dondeVive == "R" and estadoCivil == "C" and cantidadDeHijos < 2:
     print("APROBADO")
else:
     print("RECHAZADO")