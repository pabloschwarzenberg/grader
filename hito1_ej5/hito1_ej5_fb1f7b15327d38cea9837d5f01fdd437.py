from os import system
system("cls")

def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-rut_reverso]
    multiplicador = 2
    suma = 0
    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
            digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        return "K"
    elif digito_verificador == 11:
        return "0"
    else:
        return str(digito_verificador)

numero_rut = int(input("Ingrese un número de RUT: "))
dv = calcular_digito_verificador(numero_rut)
print("dv =", dv)      