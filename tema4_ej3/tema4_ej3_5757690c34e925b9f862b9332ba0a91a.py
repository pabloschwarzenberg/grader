def jerigonzo(string):
    resultado = ""
    vocales = "aeiouAEIOU"
    
    for letra in string:
        resultado += letra
        if letra in vocales:
            resultado += "p" + letra.lower()
    
    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido: ", texto_traducido)
         