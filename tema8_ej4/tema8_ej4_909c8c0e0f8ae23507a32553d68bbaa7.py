def rot13(palabra):
    voc = "abcdefghijklmnopqrstuvwxyz"
    cript = voc[13:]+voc[:13]
    rot_palabra = lambda c: voc[cript.find(c)] if cript.find(c)>-1 else c
    return ''.join( rot_palabra(c) for c in palabra ) 

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           