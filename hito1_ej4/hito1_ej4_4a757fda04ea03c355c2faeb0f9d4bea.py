def binario(decimal):
    binario2 = ''
    while decimal // 2 != 0:
        binario2 = str(decimal % 2)+ binario2
        decimal = decimal // 2
    print('resultado = {}'. format(str(decimal)+binario2))
    # return str(decimal) + binario


numero = eval(input('ingrese el numero que desea convertir '))
binario(numero)