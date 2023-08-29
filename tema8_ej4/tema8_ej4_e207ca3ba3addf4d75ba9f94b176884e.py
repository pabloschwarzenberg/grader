def rot13(palabra):
    resultado = ""
    
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                nueva_letra = chr((ord(letra) - 97 + 13) % 26 + 97)
            else:
                nueva_letra = chr((ord(letra) - 65 + 13) % 26 + 65)
            resultado += nueva_letra
        else:
            resultado += letra
    
    return resultado

# Ejemplo de uso
texto = "Hola, mundo!"
texto_encriptado = rot13(texto)
print(texto_encriptado)
