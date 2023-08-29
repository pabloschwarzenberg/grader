def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
   
def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if caracter.isalpha():
            ascii_base = ord('a') if caracter.islower() else ord('A')
            encriptado = (ord(caracter) - ascii_base + 13) % 26 + ascii_base
            resultado += chr(encriptado)
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
    

           