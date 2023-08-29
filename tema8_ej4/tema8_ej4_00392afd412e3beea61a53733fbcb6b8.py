def rot13(palabra):
    tuna = 'ABCDEFGHIJKLM'
    mayo = 'NOPQRSTUVWXYZ'
    vianesa = dict(zip(tuna + mayo, mayo + tuna))
    a = ''.join(vianesa.get(x.upper(), x) for x in palabra)

    return a.lower()


if __name__ == "__main__":
    palubria = input("Ingresa la palabra que quieras encriptar: ")
    resultado = rot13(palubria)
    print("El resultado es: ", resultado)
