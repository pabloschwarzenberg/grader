#Cálculo del dígito verificador de un rut
rut = input("Ingresa el RUT (sin dígito verificador): ")

if not rut.isdigit() or int(rut) <= 0:
    print("RUT inválido. Por favor, ingresa un número positivo.")
else:
    rut = rut[::-1]
    multiplicar = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * multiplicar
        multiplicar = multiplicar + 1 if multiplicar < 7 else 2

    dv = 11 - (suma % 11)
    if dv == 10:
        dv = 'K'
    elif dv == 11:
        dv = 0

    print("dv =", dv)