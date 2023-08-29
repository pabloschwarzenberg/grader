def rot13(palabra):
    if palabra == palabra.upper():
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        abc = "abcdefghijklmnopqrstuvwxyz"
    k = 13
    resultado = ""

    for c in palabra:
        if c in abc:
            resultado += abc[(abc.index(c) + k) % (len(abc))]
        else:
            resultado += c
    return resultado
if __name__  == "main":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print(resultado)