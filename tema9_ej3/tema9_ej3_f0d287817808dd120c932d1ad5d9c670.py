def conversion(n_binario):
    colocacion = 0
    n_decimal = 0
    n_binario = n_binario[::-1]
    for cifra in n_binario:
        operatoria = 2**(colocacion)
        n_decimal += int(cifra) * operatoria
        colocacion += 1
    return n_decimal


if __name__ == "__main__":
    x=int(2)
    y=int(10)
    oracion = ""
    n_ingresado = input("Ingresa un número binario: ")
    i=len(n_ingresado)
    while x < (i-2):
        n_binario = (n_ingresado[x:y])
        n_decimal = conversion(n_binario)
        variable_1 = (n_decimal)
        binario_ascii = chr(variable_1)
        oracion = oracion + binario_ascii
        x = y+2
        y = x+7
    print(oracion)
    

         