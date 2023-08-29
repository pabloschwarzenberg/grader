def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

def rot13(palabra):
    resultado = ""
    
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                nueva_letra = chr((ord(letra) - 97 + 13) % 26 + 97)
            else:
                nueva_letra = chr((ord(letra) - 65 + 13) % 26 + 65)
        else:
            nueva_letra = letra
        
        resultado += nueva_letra
    
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

#FIN