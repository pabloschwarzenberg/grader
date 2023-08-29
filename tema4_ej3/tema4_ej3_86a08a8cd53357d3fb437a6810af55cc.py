def jerigonzo(string):
    vocales = ["a","e","i","o","u"]
    letras = list(string)
    palabra = ""
    i = 0
    while i <= len(letras)-1:
        palabra += letras[i]
        for vocal in vocales:
            if letras[i] == vocal:
                palabra += "p" + vocal
        i += 1
    return palabra

if __name__ == "__main__":
    palabra = input("Palabra a traducir:")
    print(palabra, "en jerigonzo es", jerigonzo(palabra))
         