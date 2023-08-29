#Cálculo del dígito verificador de un rut
# Pedir al usuario que ingrese el número de RUT
rut = input("Ingrese el número de RUT (sin dígito verificador): ")


if not rut.isdigit() or len(rut) < 1:
    print("El número de RUT ingresado no es válido.")
else:
    
    digitos = list(map(int, rut[::-1]))

    
    suma = 0
    multiplicador = 2
    for d in digitos:
        suma += d * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    dv = 11 - (suma % 11)

    
    if dv == 10:
        dv = 'K'
    elif dv == 11:
        dv = 0

    
    print("dv =", dv)
      