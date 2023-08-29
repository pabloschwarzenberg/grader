def rot13(s):
    letras = "abcdefghijklmnopqrstuvwxyz"
    trans = letras[13:]+letras[:13]
    rot_letras = lambda c: trans[letras.find(c)] if letras.find(c)>-1 else c
    return ''.join( rot_letras(c) for c in s )
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)