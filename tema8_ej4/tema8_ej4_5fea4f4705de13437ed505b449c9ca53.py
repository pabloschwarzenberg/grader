abc="abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    n=13
    encriptado= ""
    for letra in palabra:
        suma = abc.find(letra) + n
        resto = int(suma) % len(abc)
        encriptado = encriptado + str(abc[resto])
    return encriptado
if __name__=="__main__":
    palabra = input('Ingrese la palabra que quieras encriptar: ')
    resultado = rot13(palabra)
    print('El resultado es: ', resultado)          