def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_letra = ord(letra) - ord('A')
                nueva_letra = chr((ascii_letra + 13) % 26 + ord('A'))
                resultado += nueva_letra
            else:
                ascii_letra = ord(letra) - ord('a')
                nueva_letra = chr((ascii_letra + 13) % 26 + ord('a'))
                resultado += nueva_letra
        else:
            resultado += letra
    return resultado

# Ejemplo de uso
texto_original = "Hola, esto es un ejemplo de ROT13."
texto_encriptado = rot13(texto_original)
print(texto_encriptado)

           