def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                codigo = ord(letra) - ord('a')
                nueva_posicion = (codigo + 13) % 26
                nueva_letra = chr(nueva_posicion + ord('a'))
                resultado += nueva_letra
            else:
                codigo = ord(letra) - ord('A')
                nueva_posicion = (codigo + 13) % 26
                nueva_letra = chr(nueva_posicion + ord('A'))
                resultado += nueva_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

           