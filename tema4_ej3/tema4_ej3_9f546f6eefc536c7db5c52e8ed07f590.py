def jerigonzo(string):
    vocales = ['a', 'e', 'i', 'o', 'u']
    texto_traducido = ''
    
    for letra in string:
        texto_traducido += letra
        if letra.lower() in vocales:
            texto_traducido += 'p' + letra.lower()

    return texto_traducido


if __name__ == "__main__":
    string_entrada = input("Ingresa el texto a traducir: ")
    string_traducido = jerigonzo(string_entrada)
    print("Texto traducido:", string_traducido)
         