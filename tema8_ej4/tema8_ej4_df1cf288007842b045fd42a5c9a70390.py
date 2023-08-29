def rot13(palabra):
    rot13 = ''
    for letra in palabra:
        
        if ord(letra) >= 65 and ord(letra) <= 90:
            if ord(letra) < 78:
                rot13 += chr(ord(letra) + 13)
                
            else:
                rot13 += chr(ord(letra) - 13)
                
        elif ord(letra) >= 97 and ord(letra) <= 122:
            if ord(letra) < 110:
                rot13 += chr(ord(letra) + 13)
                
            else:
                rot13 += chr(ord(letra) - 13)
        
    return rot13

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           