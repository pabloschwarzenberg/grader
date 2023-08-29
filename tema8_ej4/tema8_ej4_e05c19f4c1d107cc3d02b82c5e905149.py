def rot13(palabra):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rot13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    
    new_palabra = ''
    
    for l in palabra:
        if l in letras:
            new_palabra += rot13[letras.index(l)]
        else:
            new_palabra += l
    
    return new_palabra  

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           