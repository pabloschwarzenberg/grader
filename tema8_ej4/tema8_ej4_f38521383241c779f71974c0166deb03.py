def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyz"
    encriptado = ""

    for letra in palabra:
        encriptado += abc[(abc.find(letra)+13) % 26]
    return encriptado
           