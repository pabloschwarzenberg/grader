def cambio (decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

decimal = int(input("Introduce el número a convertir a binario : "))    
print("resultado=",cambio(decimal))