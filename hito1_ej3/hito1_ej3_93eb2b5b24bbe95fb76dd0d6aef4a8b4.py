Ingreso_peso = int(input("Ingreso en pesos: "))
Año_de_nacimiento = int(input("Año de nacimiento: "))
N_de_hijos = int(input("Numero de hijos: "))
Años_banco = int(input("Año de pertenencia al banco: "))
Estado_Civil = input("S:soltero, C:casado: ")
Vivienda = input("U:urbano, R:rural: ")
EDAD = (2021 - Año_de_nacimiento)
if Años_banco > 10 and N_de_hijos >= 2:
    print("APROBADO")

elif Estado_Civil == "C" and (N_de_hijos > 3) and(EDAD >= 45) and (EDAD <= 55):
    print("APROBADO")

elif Ingreso_peso >= 2500000 and Estado_Civil == "S" and Vivienda  == "U":
    print("APROBADO")

elif Ingreso_peso == 3500000 and Años_banco > 5:
    print("APROBADO")

elif Vivienda == "R" and Estado_Civil == "C" and N_de_hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")
      