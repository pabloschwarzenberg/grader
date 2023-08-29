def rot13(palabra):
    linea = "abcdefghijklmnopqrstuvwxyz"
    trans = linea[13:] + linea[:13]
    linea_rot = lambda c: trans[linea.find(c)] if linea.find(c) > -1 else c
    return ''.join(linea_rot(c) for c in palabra)

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
           