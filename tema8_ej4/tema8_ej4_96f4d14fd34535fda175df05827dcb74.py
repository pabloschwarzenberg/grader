def rot13(palabra):
    palabra_encriptada = ""
    for caracter in palabra:
        if caracter.isalpha():  # Verifica si el carácter es una letra
            desplazamiento_ascii = ord('a') if caracter.islower() else ord('A')
            # Determina el desplazamiento en el alfabeto según si el carácter es minúscula o mayúscula
            # ord('a') = 97, ord('A') = 65
            caracter_encriptado = chr((ord(caracter) - desplazamiento_ascii + 13) % 26 + desplazamiento_ascii)
            # Aplica el cifrado ROT13: resta el desplazamiento, agrega 13 y calcula el módulo 26 para mantenerlo en el rango de letras
            # Luego, suma el desplazamiento nuevamente para obtener el carácter encriptado
            palabra_encriptada += caracter_encriptado
        else:
            # Si el carácter no es una letra, lo agrega directamente a la palabra encriptada sin modificarlo
            palabra_encriptada += caracter
    return palabra_encriptada



           