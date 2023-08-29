def rot13(palabra):
    palabra_encriptada = ""

    # Recorrer cada carácter de la palabra
    for caracter in palabra:
        # Verificar si el carácter es una letra
        if caracter.isalpha():
            # Obtener el código ASCII del carácter
            codigo_ascii = ord(caracter)

            # Verificar si el carácter es una letra mayúscula
            if caracter.isupper():
                # Aplicar el desplazamiento ROT13 a las letras mayúsculas
                codigo_encriptado = (codigo_ascii - 65 + 13) % 26 + 65
            else:
                # Aplicar el desplazamiento ROT13 a las letras minúsculas
                codigo_encriptado = (codigo_ascii - 97 + 13) % 26 + 97

            # Obtener el carácter encriptado correspondiente al código ASCII
            caracter_encriptado = chr(codigo_encriptado)

            # Agregar el carácter encriptado a la palabra encriptada
            palabra_encriptada += caracter_encriptado
        else:
            # Mantener el carácter original
            palabra_encriptada += caracter

    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)

           