def rot13(palabra):
    resultado = ""
    
    for letra in palabra:
        if letra.isalpha():
            codigo = ord(letra.lower()) + 13
            if codigo > ord('z'):
                codigo -= 26
            resultado += chr(codigo)
        else:
            resultado += letra
    
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: {palabra_encriptada}")
