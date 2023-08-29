def rot13(palabra):
    resultado = ""
    
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_inicio = ord('A')
            else:
                ascii_inicio = ord('a')
            
            ascii_letra = ord(letra)
            ascii_encriptado = (ascii_letra - ascii_inicio + 13) % 26 + ascii_inicio
            letra_encriptada = chr(ascii_encriptado)
            resultado += letra_encriptada
        else:
            resultado += letra
    
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
           