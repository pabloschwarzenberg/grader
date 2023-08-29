#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplos = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = 0
    for i in range(len(rut)-1, -1, -1):
        digito = int(rut[i])
        multiplicador = multiplos.pop(0)
        suma += digito * multiplicador
        if len(multiplos) == 0:
            multiplos = [2, 3, 4, 5, 6, 7, 2, 3]
    verificador = 11 - (suma % 11)
    if verificador == 11:
        return 0
    elif verificador == 10:
        return 'K'
    else:
        return verificador
rut = input("Ingrese el número de RUT sin el dígito verificador: ")
dv = calcular_digito_verificador(rut)
print("dv =", dv)      