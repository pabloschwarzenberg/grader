# Entrada
ingreso = int(input("Ingrese sus ingresos (en peso chileno):"))
nacimiento = int(input("Ingrese su año de nacimiento:"))
hijos = int(input("Ingrese la cantidad de hijos:"))
banco =  int(input("Ingrese la cantidad de años que pertenece al banco:"))
estado = input("Ingrese una S si esta soltero o una C si se encuentra casado:")
lugar = input("Ingrese U si vive en ciudad o R si vive en campo:")
edad = (2022 - nacimiento)

# Condiciones

if banco > 10 and hijos >= 2:
    print("APROBADO") 

elif estado == "C" and hijos > 3 and edad > 45 and edad < 55:
    print("APROBADO")

elif ingreso > 25 * 10**5 and estado == "S" and lugar == "U":
    print("APROBADO")

elif ingreso > 35 * 10**5 and banco > 5:
    print("APROBADO")

elif lugar == "R" and estado == "C" and hijos < 2:
    print("APROBADO")

else: print("RECHAZADO")