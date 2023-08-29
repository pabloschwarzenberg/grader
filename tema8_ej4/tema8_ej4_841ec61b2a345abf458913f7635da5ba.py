def rot13(palabra):
    resul = ""
    
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                nletra = chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
            else:
                nletra = chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            nletra = letra
        
        resul += nletra
    
    return resul
    
    
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           