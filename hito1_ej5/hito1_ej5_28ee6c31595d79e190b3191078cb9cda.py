#Cálculo del dígito verificador de un rut
def cal_dig(rut):
    rut = str(rut)
    mul = [2, 3, 4, 5, 6, 7]
    suma = 0
    indice = 0

    for digito in reversed(rut):
        suma += int(digito) * mul[indice]
        indice = (indice + 1) % 6

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return 'K'
    else:
        return digito_verificador

rut = input("Ingrese el RUT sin dígito verificador: ")
digito_verificador = cal_dig(rut)
print("dv =", digito_verificador)