# Entradas
ingresos = int(input("Ingrese cuanto gana: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
banco = int(input("Ingrese cuantos años lleva en el banco: "))
ec = input("Ingrese su estado civil en 'S': Soltero o 'C': Casado: ")
casa = input("Ingrese si vive en 'R': campo o 'U' ciudad: ")

# Procesamiento
ec = ec.lower()
casa = casa.lower()
edad = 2022-nacimiento

if ingresos > 3500000:
    if banco > 5:
        print("APROBADO")
elif casa == "r" or "campo":
    if hijos < 2 and ec == "c" or "casado":
        print("APROBADO")
elif hijos >= 2:
    if banco > 10:
        print("APROBADO")
elif ec == "c" or "casado":
    if hijos > 3 and edad in [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]:
        print("APROBADO")
elif ingresos > 2500000:
    if ec == "s" or "soltero" and casa == "u" or "ciudad":
        print("APROBADO")

else:
    print("RECHAZADO")