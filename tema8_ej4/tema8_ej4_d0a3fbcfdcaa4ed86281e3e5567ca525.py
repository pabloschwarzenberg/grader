def rot13(palabra):
    abcdario = "abcdefghijklmnopqrstuvwxyz"
    tran = abcdario[13:] + abcdario[:13]
    rot_abcd = lambda c: tran[abcdario.find(c)] if abcdario.find(c)>-1 else c
    return ''.join( rot_abcd(c) for c in palabra )
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           