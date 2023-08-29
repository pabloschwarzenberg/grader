def rot13(palabra):
    palabra_encriptada = ""
    
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                indice = (ord(letra) - ord('a') + 13) % 26
                letra_encriptada = chr(ord('a') + indice)
            else:
                indice = (ord(letra) - ord('A') + 13) % 26
                letra_encriptada = chr(ord('A') + indice)
        else:
            letra_encriptada = letra
        
        palabra_encriptada += letra_encriptada
    
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
