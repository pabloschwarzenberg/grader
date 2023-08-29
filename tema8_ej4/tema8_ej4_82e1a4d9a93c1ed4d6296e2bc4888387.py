def rot13(palabra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    palabraCodificada = ''
    for letra in palabra:
        posicion = alfabeto.index(letra)
        letraSutituta = alfabeto[posicion+13]
        palabraCodificada += letraSutituta
    return palabraCodificada