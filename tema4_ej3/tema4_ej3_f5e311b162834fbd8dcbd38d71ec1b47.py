def jerigonza(original):
     traducida = ""
    for letra in original:
        traducida += letra
        if letra.lower() in "aeiou":
            traducida += "p" + letra
    return traducida

if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    traducida = jerigonza(palabra)
    print(traducida)

         