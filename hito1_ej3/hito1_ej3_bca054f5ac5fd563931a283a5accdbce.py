Ingreso = float(input("Ingrese su ingreso en clp (Unidad de Peso Chileno).........: $" ))
Año_nacimiento = int(input("Ingrese su año de nacimiento........................:  " ))
Nro_hijos = int(input("Ingrese la cantidad de hijos que posee...................:  " ))
Años_banco = int(input("Ingrese la cantidad de años de pertenencia en el banco..:  " ))
Años_cliente= 2022 - Año_nacimiento

print("Soltero (S)")
print("Casado  (C)")
Estado_civil =(input("Ingrese la alternativa de su estado civil.................:  " ))

print("Zona Rural...(R)")
print("Zona Urbana..(U)")
Zona =(input("Ingrese la alternativa de donde vive..............................:  " ))
contadoraceptado = 0

if contadoraceptado == 0:
    if Años_banco > 10:
        if Nro_hijos >= 2:
            contadoraceptado = contadoraceptado + 1
            print("APROBADO")

if contadoraceptado == 0:
    if Estado_civil == "C":
        if Nro_hijos > 3:
            if Años_cliente > 45 and Años_cliente < 55:
                contadoraceptado = contadoraceptado + 1
                print("APROBADO")

if contadoraceptado == 0:
    if Ingreso > 2500000:
        if Estado_civil == "S":
            if Zona == "U":
                print("APROBADO")
                contadoraceptado = contadoraceptado + 1

if contadoraceptado == 0:
    if Ingreso > 3500000:
        if Años_banco > 5:
            print("APROBADO")
            contadoraceptado = contadoraceptado + 1

if contadoraceptado == 0:
    if Zona == "R":
        if Estado_civil == "C":
            if Nro_hijos < 2:
                print("APROBADO")
                contadoraceptado = contadoraceptado + 1

if contadoraceptado == 0:
    print("RECHAZADO")
