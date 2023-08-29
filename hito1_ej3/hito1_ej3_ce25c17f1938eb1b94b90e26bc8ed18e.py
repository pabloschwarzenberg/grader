#Aprobación de créditos
ingreso = int(input("Ingreso en pesos: "))
anhos = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
anhos_banco = int(input("Año de pertenencia al banco: "))
estado_civil = input("S:soltero, C:casado: ")
vivienda = input("U:urbano, R:rural: ")
edad = (2021 - anhos)
if anhos_banco > 10 and hijos >= 2:
    print("aprobado")
elif ingreso >= 2500000 and estado_civil == "S" and vivienda  == "U":
    print("aprobado")
elif estado_civil == "C" and (hijos > 3) and(edad >= 45) and (edad <= 55):
    print("aprobado")
elif vivienda == "R" and estado_civil == "C" and hijos < 2:
    print("aprobado")
elif ingreso == 3500000 and anhos_banco > 5:
    print("aprobado")
else:
    print("rechazado")
#puse las ñ como nh porque la ñ no me la reconocía
#la verdad no sé por qué me tira error en cuatro casos, los probé en python y todos me funcionan...
