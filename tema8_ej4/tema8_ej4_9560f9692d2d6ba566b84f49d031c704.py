def rot13(palabra):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(len(palabra)):
        indice = (abecedario.index(palabra[i]) + 13) % 26
        result += abecedario[indice]
    return result


if __name__ == '__main__':
    palabra = input('Ingresa la palabra que quieras encriptar: ').lower()
    resultado = rot13(palabra)
    print('El resultado es: ', resultado)