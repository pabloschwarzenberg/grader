###Entrada de datos:
ingreso = int(input("Escriba su ingreso:  "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos que usted posea: "))
aBanco = int(input("Ingrese su pertenencia en años con nosotros: "))
eCivil = input("Ingrese su estado civil, soltero o casado (S o C): ")
camp_city = input("Ingrese si su recidencia es rural o urbano (R o U): ")
edad = (2021 - nacimiento)
###Procedimiento:

if aBanco > 10 and hijos >= 2:
    print("APROBADO")#Salida
elif eCivil == "C" and hijos > 3 and edad in range(45,55):
    print("APROBADO")#Salida
elif ingreso > 2500000 and eCivil == "S" and camp_city == "U":
    print("APROBADO")#Salida
elif ingreso > 3500000 and aBanco > 5:
    print("APROBADO")#Salida
elif camp_city == "R" and eCivil == "C" and hijos < 2:
    print("APROBADO") #Salida
else:
    print("RECHAZADO")#Salida