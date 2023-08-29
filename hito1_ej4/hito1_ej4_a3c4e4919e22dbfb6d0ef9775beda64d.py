def nBinario(decimal):
    if decimal <=0:
       return "0"
    binario = ""

#validar datos

    while decimal > 0:
            residuo = int(decimal % 2)
            decimal = int(decimal / 2)
            binario = str(residuo) + binario
    return binario

#imprimir resultado X
nDecimal = int(input("introduzca un número decimal: "))
nBinario = nBinario(nDecimal)
print("resultado=", nBinario)