    def rot_13(cad):
    orig = 'ABCDEFGHIJKLM'
    tgt = 'NOPQRSTUVWXYZ'
    rotmapper = dict(zip(orig + tgt, tgt + orig))
    return ''.join(rotmapper.get(x.upper(), x) for x in cad)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           