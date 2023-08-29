#Aprobación de créditos
ingr= int(input("Escriba sus ingresos en pesos:"))
ano_nacimiento=int(input("Ingrese su año de nacimiento:"))
num_hijos=int(input("numero de hijos:"))
ano_banco=int(input("Ingrese los años en el banco:"))
estado_civil = input("S si es soltero; y C si esta casado:")
vivienda=input("Ingrese U si vive en un lugar urbano o R si vive en un lugar rural:")
if ano_banco >= 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil.upper() == "C" and num_hijos > 3 and ano_nacimiento >= 45 or ano_nacimiento <= 55:
    print("APROBADO")
elif ingr < 2500000 and estado_civil.upper() == "S" and vivienda.upper() == "U":
    print("APROBADO")
elif ingr > 3500000 and ano_banco > 5:
    print("APROBADO")
elif vivienda.upper() == "R" and estado_civil.upper() == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")   