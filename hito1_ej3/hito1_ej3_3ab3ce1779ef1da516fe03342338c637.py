#Aprobación de créditos
ingreso = int(input("Ingreso: "))
nacimiento = int(input("Año de nacimiento: "))
edad=(2022-nacimiento)
hijos = int(input("Cantidad de hijos: "))
pertenencia = int(input("Años de pertenencia: "))
estado = input("Estado civil: ")
vivencia = input("Vive en Rural/Urbano: ")
if (pertenencia>=10 and hijos>=2):
    print("APROBADO")
elif (estado=="C" and hijos>=3 and edad>=45 and edad<=55):
    print("APROBADO")
elif (ingreso>=2500000 and estado=="S" and vivencia=="U"):
    print("APROBADO")
elif (ingreso>=2500000 and pertenencia>=5):
    print("APROBADO")
elif (vivencia=="R" and estado=="C" and hijos<=2):
    print("APROBADO")
else:
    print("REPROBADO")