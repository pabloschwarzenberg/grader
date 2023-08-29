ingreso = int(input("¿Cual es su ingreso mensual?: "))
nacimiento = int(input("¿Cual es su año de nacimiento?: "))
hijos = int(input("¿Cuantos hijos tiene?: "))
antiguedad = int(input("¿Hace cuantos años es cliente del banco?: "))
#estado civil
soltero_casado = input("Ingrese S si es soltero, C si es casado: ")
#donde vive
urbano_rural = input("Ingrese U si vive en sector es urbano, R si es rural: ")

if antiguedad > 10 and hijos >= 2:
    print("APROBADO")
elif soltero_casado == "C" and hijos > 3 and  nacimiento == range(1966,1976):
    print("APROBADO")
elif ingreso > 2500000 and soltero_casado == "S" and urbano_rural == "U":
    print("APROBADO")
elif ingreso > 3500000 and antiguedad > 5:
    print("APROBADO")
elif urbano_rural == "R" and soltero_casado == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      