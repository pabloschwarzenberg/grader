def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


if __name__ == "__main__":
    numero = int(input('Introduce el número a convertir a binario: '))
    bina = binarizar(numero)
    print("resultado=", bina)
