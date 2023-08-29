def rot13(palabra):
    encriptada = ''
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.islower():
                encriptada += chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
            else:
                encriptada += chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            encriptada += caracter
    return encriptada

palabra = input('Ingresa una palabra: ')
palabra_encriptada = rot13(palabra)
print('Palabra encriptada:', palabra_encriptada)
