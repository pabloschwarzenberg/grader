#Aprobación de créditos
ingresos_cliente = int(input("Digite sus ingresos mensuales en pesos: "))
anio_nac_cliente = int(input("Ingrese su año de nacimiento "))
hijos_cliente = int(input("Digite la cantidad de hijos que tiene: "))
anios_cliente_banco = int(input("Digite cuantos años lleva en el banco: "))
estado_civil_cliente = input("Estado civil (\"S\": soltero, \"C\", casado)")
domicilio = input("Vive en campo o ciudad? (\"U\": urbano, \"R\": rural)")
edad = 2021-anios_cliente_banco

if(anios_cliente_banco > 10 and hijos_cliente >= 2):
    print("APROBADO")
elif(estado_civil_cliente == "C" and hijos_cliente > 3 and (edad <= 55 or edad >=45)):
    print("APROBADO")
elif(ingresos_cliente > 2500000 and estado_civil_cliente == "S" and domicilio == "U"):
    print("APROBADO")
elif((ingresos_cliente > 3500000) and (anios_cliente_banco > 5)):
    print("APROBADO")
elif(domicilio == "R" and estado_civil_cliente == "C" and hijos_cliente < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
