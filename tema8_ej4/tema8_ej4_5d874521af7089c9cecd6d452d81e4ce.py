def rot13(palabra):
    encriptada = ""
    letras_min = "abcdefghijklmnopqrstuvwxyz"
    letras_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                indice = letras_min.index(letra)
                encriptada += letras_min[(indice + 13) % 26]
            else:
                indice = letras_may.index(letra)
                encriptada += letras_may[(indice + 13) % 26]
        else:
            encriptada += letra
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)