def rot13(texto):
    palabra = "abcdefghijklmnopqrstuvwxyz"
    trans = palabra[13:]+palabra[:13]
    rot_palabra = lambda c: trans[palabra.find(c)] if palabra.find(c)>-1 else c
    return ''.join(rot_palabra(c) for c in texto )

if __name__== '__main__':
    texto=input("Ingrese la palabra que quiere encriptar:")
    texto.lower()
    resultado=rot13(texto)
    print ("El resultado es:", resultado)