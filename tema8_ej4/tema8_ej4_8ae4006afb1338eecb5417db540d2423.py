def rot13(palabra):
    orig = 'abcdefghijklm'
    tgt = 'nopqrstuvwxyz'
    rotmapper = dict(zip(orig + tgt, tgt + orig))
    return ''.join(rotmapper.get(x) for x in palabra)
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           