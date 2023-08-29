#Aprobación de créditos
ingreso = eval(input("ingreso:\n"))
agno_nacimiento = eval(input("agno de nacimiento:\n"))
cantidad_hijos = eval(input("numero de hijos:\n"))
agno_banco = eval(input("agno de pertenencia al banco:\n"))
estado_civil = str(input("(S:soltero, C:casado):\n"))
lugar_residencia = str(input("(U:urbano, R:rural):\n"))

edad = 2020 - agno_nacimiento

if(agno_banco >= 10 and cantidad_hijos >= 2):
    print("APROBADO")

elif (estado_civil == "C") and (cantidad_hijos >= 3) and (45 <= edad <= 45):
    print("APROBADO")

elif ingreso >= 2500000 and estado_civil == "S" and lugar_residencia == "U":
    print("APROBADO")

elif ingreso >= 3500000 and agno_banco >= 5:
    print("APROBADO")

elif lugar_residencia == "R" and estado_civil == "C" and cantidad_hijos <= 2:
    print("APROBADO")

else:
    print("RECHAZADO")

      