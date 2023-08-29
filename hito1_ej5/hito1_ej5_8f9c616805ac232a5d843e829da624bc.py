#Cálculo del dígito verificador de un rutrut = input("Ingrese un número de RUT: ")
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.zfill(8)
    multiplicadores = [3, 2, 7, 6, 5, 4, 3, 2]
    suma = sum(int(digito) * multiplicador for digito, multiplicador in zip(rut, multiplicadores))
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        dv = "0"
    elif dv == 10:
        dv = "K"
    return str(dv)

# Solicitar el ingreso del RUT al usuario
rut = input("Ingresa el RUT sin dígito verificador: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
