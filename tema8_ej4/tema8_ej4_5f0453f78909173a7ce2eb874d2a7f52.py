def rot13(palabra):
    letras = "abcdefghijklmnopqrstuvwxyz"
    encrip = letras[13:]+letras[:13]
    encrip_letra = lambda x: encrip[letras.find(x)] if letras.find(x)>-1 else x
    return ''.join(encrip_letra(x) for x in palabra)
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           