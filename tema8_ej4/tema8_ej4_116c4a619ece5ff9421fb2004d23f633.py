def rot13(palabra):
    nueva_l = 0
    pos = 0
    for ncaracter, in (palabra):
        ncaracter = ord(ncaracter)+13
        if (ncaracter) >= 123:
            caracter_13 = ((ncaracter-123)+97)
            
        else:
            caracter_13 = ncaracter
        palabra = palabra[:pos] + chr(caracter_13) + palabra[pos+1:] 
        pos = pos+1
    return palabra    
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           