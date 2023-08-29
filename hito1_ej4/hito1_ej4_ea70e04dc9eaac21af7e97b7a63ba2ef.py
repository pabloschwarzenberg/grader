def cambio_base(decimal):
    conversion = ''
    while decimal // 2 != 0:
        conversion = str(decimal % 2) + conversion
        decimal = decimal // 2
    return str(decimal) + conversion

numero = int(input('Introduce el binario '))
print("resultado=",cambio_base(numero))