#Datos de el cliente 
ingreso = int(input("Ingreso mensual en pesos : "))
añoN = int(input("Ingresa año de nacimiento : "))
nHijos = int(input("Ingrese numero de hijos : "))
añoEnB = int(input("Ingrese numero de años en nuestro banco : "))
eCivil = input("Estado civil (S: Para soltero y C: Para casado) : ")
viveUR = input("Vive en (U:Para localidad urbana R: Para localidad rural) : ")
#Operaciones
edad = 2020 - añoN
#Condicionales
if añoEnB >= 10 and nHijos >= 2 :
    print("APROBADO")
if (eCivil == "C" or eCivil == "c") and nHijos > 3 and (edad >= 45 and edad <= 55): 
    print("APROBADO")
if ingreso >= 2500000 and (eCivil == "S" or eCivil == "s") and (viveUR == "R" or viveUR == "r"):
    print("APROBADO")
if ingreso >= 3500000 and añoEnB >= 5 :
    print("APROBADO")
if (viveUR == "R" or viveUR == "r") and (eCivil == "C" or eCivil == "c") and nHijos < 2 :
    print("APROBADO")
else:
    print("Credito RECHAZADO")
     