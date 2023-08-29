def rot13(palabra):
    abc = 'abcdefghijklm'
    nop = 'nopqrstuvwxyz'
    cifrado = dict(zip(abc + nop, nop + abc))
    return ''.join(cifrado.get(x.lower(), x) for x in palabra)
 
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ").lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           