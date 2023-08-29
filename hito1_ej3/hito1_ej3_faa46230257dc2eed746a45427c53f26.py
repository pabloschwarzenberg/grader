#Aprobación de créditos
ingresos = int(input("Ingreso(en pesos): "))
Nacimiento = int(input("Ingrese fecha de nacimiento: "))
Hijos = int(input("Ingrese cantidad de hijos: "))
TiempoBanco = int(input("Indique el tiempo en el banco: "))
EC = (input("Ingrese estado civil 'S' o 'C': "))
vivienda = input("Ingrese si vive en campo o ciudad 'U' o 'R': ")

if TiempoBanco > 10 and Hijos >=2:
    print("APROBADO")
elif EC == "C" and Hijos >=3 and Nacimiento >= 1966 and Nacimiento <= 1976:
    print("APROBADO")
elif ingresos > 2500000 and EC == "S" and vivienda == "U":
    print("APROBADO")
elif vivienda == "R" and EC == "C" and Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      