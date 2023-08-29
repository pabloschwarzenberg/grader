#Escribe un programa que reciba como dato un número que representará un rut al que debe calcularle el dígito verificador.
from os import system
system ("cls")
def calcular_digito_verificador(rut):
    rut_invertido = str(rut)[::-1]  
    multiplicador = 2
    suma = 0

    for digito in rut_invertido:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    resto = suma % 11
    digito_verificador = 11 - resto
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'k'

    return digito_verificador

rut = (int(input("Ingrese rut sin digito verificador: ")))
dv = calcular_digito_verificador(rut)
print("dv =", dv)
