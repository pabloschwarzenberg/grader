#Cálculo del dígito verificador de un rut
def digito_verificador(rut):
    rutinverso = str(rut)[::-1] 
#invertir el rut
    f = 2
    s = 0
#dar valores a variables
    for digito in rutinverso:
        s += int(digito) * f
        f = f + 1 if f < 7 else 2
#usar el for in con el numero entero en el rut inverso y aplica la formula
    resto = s % 11
    verificador = 11 - resto if resto != 0 else 0

    if verificador == 10:
        return 'K'
    else:
        return str(verificador)
#utilizar las condicionales para sacar el digito y dar si termina en K o numero
rut = int(input("Ingrese un número de Rut: "))
#preguntar el rut que se desea sacar el codigo verificador

digver = digito_verificador(rut)
#calcular el digito verificador

print("dv =", digver)
#imprimir el resultado