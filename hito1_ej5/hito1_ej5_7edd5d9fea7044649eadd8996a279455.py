#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.zfill(8)

    multiplicadores = [3, 2, 7, 6, 5, 4, 3, 2]  
    suma = 0

    for i in range(8):
        suma += int(rut[i]) * multiplicadores[i]

    resto = suma % 11
    dv = 11 - resto

    if dv == 11:
        return 'dv=0'
    elif dv == 10:
        return 'dv=K'
    else:
        return 'dv=' + str(dv)

rut = input("Ingrese el RUT (sin dígito verificador): ")
dv = calcular_digito_verificador(rut)
print(dv)