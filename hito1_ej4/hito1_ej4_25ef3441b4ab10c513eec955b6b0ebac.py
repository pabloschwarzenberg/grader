def binarioa(variable):
    binario = ''
    while variable // 2 != 0:
        binario = str(variable % 2) + binario
        variable = variable // 2
    return str(variable) + binario
numero = int(input('Introduce el número a convertir a binario: '))
print("resultado="+binarioa(numero))