def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nop = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    cambio = dict(zip(abc, nop))
    return ''.join(cambio.get(char, char) for char in palabra)
    pass

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)