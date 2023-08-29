#Aprobación de créditos
ingreso = int(input("Ingrese sus ingresos:"))
fecha = int(input("Ingrese su año de nacimiento:"))
hijos = int(input("Ingrese su numero de hijos:"))
pertenencia = int(input("Ingrese años de pertenencia al banco:"))
estado = str(input("Ingrese su estado civil: "))
lugar = str(input("Ingrese lugar donde vive si es campo o rural:"))


R = str(lugar)
U = str(lugar)
S = str(estado)
C = str(estado)

ano = 2020 - fecha - 1     #Revisar la edad sacarla bien

#se aprueba el credito

if((pertenencia >= 10) and (hijos >= 2)):
     print("APROBADO")
elif((estado == C) and (hijos >= 3) and (45 >= ano) and (ano <= 55)):
    print("APROBADO")
elif((ingreso >= 2500000) and (estado == S) and (lugar == R)):
    print("APROBADO")
elif((ingreso >= 3500000) and (pertenencia >= 5)):
    print("APROBADO")
elif((lugar == U) and (estado == C) and (hijos <= 2)):
    print("APROBADO")
else:
    print("RECHAZO")