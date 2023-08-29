## ENTRADA DE DATOS - PROCESO - SALIDA

## FUNCIÓN

def rot13(palabra):
    palabra_encriptada = ""
    for char in palabra:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            rotated_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            palabra_encriptada += rotated_char
        else:
            palabra_encriptada += char
    return palabra_encriptada

## LLAMADA FUNCIÓN E IMPRESIÓN EN PANTALLA

if __name__ == "__main__":
    palabra = input("Ingrese la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
           