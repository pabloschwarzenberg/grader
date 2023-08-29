#Aprobación de créditos
#Entradas
ingreso=int(input("Introduzca su ingreso mensual en pesos: "))
nacimiento=int(input("Introduzca su año de nacimiento: "))
hijos=int(input("Introduzca el número de hijos: "))
anos=int(input("Introduzca los años de pertenencia al banco: "))
eCivil=input("Indique su estado Civil [S] soltero y [C] casado: ")
ubicacion=input("Indique si vive en la ciudad [U] o en el campo [R]: ")
edad= 2020 - nacimiento

if anos > 10 and hijos >= 2:
    print("APROBADO")

elif (eCivil == "C" or eCivil == "c")and hijos > 3 and (edad > 45 and edad < 55):
    print("APROBADO")
    
elif ingreso > 2500000 and (eCivil == "S" or eCivil == "s") and (ubicacion == "U" or ubicacion == "u"):
    print("APROBADO")

elif ingreso > 3500000 and anos > 5:
    print("APROBADO")

elif (ubicacion == "R" or ubicacion == "r") and (eCivil == "C" or eCivil == "c") and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")      