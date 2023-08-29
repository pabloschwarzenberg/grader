ingreso= int(input("Ingrese su ingreso mensual: "))
anio_nacimiento= int(input("Ingrese su año de nacimiento: "))
num_h: int(input("Ingrese la cantidad de hijos que tiene: "))
anios_banco= int(input("Ingrese la cantidad de años que lleva en el banco: "))
print(("S): Soltero, C): Casado"))
estado_civil= input("Para las anteriores opciones ingrese su estado civil: ")
print("U): Ciudad/Urbano , R) Campo/Rural")
vivienda= input("Segun lo anterior, ingrese donde vive: ")
estado_civil.lower()
vivienda.lower()
while True:
    if anios_banco > 10:
        if num_h >= 2:
            print("Su credito ha sido APROBADO")
            break
    if estado_civil == "c":
        if num_h > 3:
            if (anio_nacimiento-2020) >= 45 and (anio_nacimiento-2020) <= 55:
                print("Su credito ha sido APROBADO")
                break
    if ingreso > 2500000:
        if estado_civil== "s":
            if vivienda == "u":
                print("Su credito ha sido APROBADO")
                break
    if ingreso > 3500000:
        if anios_banco > 5:
            print("Su credito ha sido APROBADO")
            break
    if vivienda == "r":
        if estado_civil == "c":
            if num_h < 3:
                print("Su credito ha sido APROBADO")
                break
    else:
        print("Su credito ha sido RECHAZADO")
        break