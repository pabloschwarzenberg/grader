def rot13(palabra):
    abc = 'abcdefghijklmnopqrstuvwxyz'*2

    encriptada = ''

    for letra in palabra:
        if letra in abc:
            encriptada += abc[abc.index(letra) + 13]
        
        else:
            encriptada += letra
    
    return encriptada  

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           