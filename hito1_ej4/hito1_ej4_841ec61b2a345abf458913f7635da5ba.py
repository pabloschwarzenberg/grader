deci= int(input("Ingrese un número decimal: "))

binario = []

while deci > 0:
    residuo = deci % 2
    binario.append(residuo)
    deci= deci // 2

binario.reverse()

binastr = ''.join(str(digito) for digito in binario)

print("Resultado=", binastr)