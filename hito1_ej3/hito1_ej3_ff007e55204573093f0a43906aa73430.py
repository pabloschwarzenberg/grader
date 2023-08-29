#Aprobación de créditos

#Entrada
ingreso = int(input("Ingrese sus numero de ingresos: "))
anonaci = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese sus numero de hijos: "))
anopert = int(input("Ingrese sus años de pertenencia al banco: "))
estciv = input("Ingrese su estado civil (S/C) : ")
vivienda = input("Ingrese donde vive (U/R): ")

#Condiciones de Aprovacion
if anopert >= 10 and hijos >= 2:
    print("Credito APROBADO")
elif estciv == "C" and anonaci >= 45 and anonaci <= 55:
    print("Credito APROBADO")
elif ingreso >= 2500000 and estciv == "S" and vivienda == "U":
    print("Credito APROBADO")
elif ingreso >= 3500000 and anopert >= 5:
    print("Credito APROBADO")
elif vivienda == "R" and estciv == "C" and hijos <= 2:
    print("Credito APROBADO")
                      
else:
    print("Credito RECHAZADO")
