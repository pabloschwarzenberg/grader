#Aprobación de créditos
ingreso = eval(input("ingreso:\n "))
nacimiento = eval(input("fecha de nacimiento:\n "))
hijos = eval(input("cantidad de hijos:\n "))
banco = eval(input("agno de pertenecia al banco:\n "))
estado_civil = str(input("(S:soltero, C:casado)\n "))
lugar_de_residencia = str(input("U:urbano, R:rural\n "))

edad = 2020 - nacimiento

if(banco >= 10 and hijos >= 2):
    print("APROBADO")

elif(estado_civil == "c") and (hijos >= 3) and (45 <= edad <= 55):
    print("APROBADO")

elif ingreso >= 2500000 and estado_civil == "S" and lugar_de_residencia == "U" :
    print("APROBADO")

elif ingreso >=3500000 and banco >= 5:
    print("APROBADO")

elif lugar_de_residencia == "R" and estado_civil == "C" and hijos <= 2:
    print("APROBADO")

else:
    print("RECHAZADO")