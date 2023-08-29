ingreso = int(input("Digite su ingreso en pesos:\n"))
nacimiento = int(input("Ingrese su Año de nacimiento:\n"))
hijo = int(input("Cuantos hijo/as tiene:\n"))
pertenece = int(input("Cuantos años ha pertenecido al banco:\n"))
estado = input("ingrsese su estado civil (soltero: S / casado: C):\n").upper()
vive = input("Usted vive en campo o ciudad (urbano: U / rural:  R):\n").upper()

if pertenece > 10 and hijo >= 2:
    print("APROBADO")
elif estado == "C" and hijo > 3 and nacimiento <= 55 and nacimiento >= 45:
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and vive == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenece > 5:
    print("APROBADO")
elif vive == "R" and estado == "C" and hijo < 2:
    print("APROBADO")
else:
    print("RECHAZADO")