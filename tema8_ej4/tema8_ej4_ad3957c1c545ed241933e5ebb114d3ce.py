def rot13(palabra):
    abc = 'abcdefghijklm'
    nop = 'nopqrstuvwxyz'
    cifrado = dict(zip(abc + nop, nop + abc))
    return ''.join(cifrado.get(x.lower(), x) for x in palabra)
 
#palabra= input("Ingresa la palabra que quieras encriptar:")
#palabra.lower()
#resultado=rot13(palabra)
#print("El resultado es: ",resultado)


           