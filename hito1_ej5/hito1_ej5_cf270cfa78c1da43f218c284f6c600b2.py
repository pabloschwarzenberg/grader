#Cálculo del dígito verificador de un rut

rut = input("Ingrese un número de RUT (sin dígito verificador): ")

if not rut.isdigit() or len(rut) < 1:
    print("El RUT ingresado no es válido.")
else:
    rut = rut[::-1]
    multiplicador = 2
    suma = 0

    for d in rut:
        suma += int(d) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = "K"

    print("dv=" + str(dv))
