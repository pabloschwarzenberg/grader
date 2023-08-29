def jerigonzo(texto):
    texto = list(texto)
    print(texto)
    vocales = ['a','e','i','o','u']
    palabra_cambiada = ""
    for a in texto:
        print(a)
        if a in vocales:
            palabra_cambiada += a+'p'+a
        else:
            palabra_cambiada += a
    return ''.join(palabra_cambiada)

if __name__ == "__main__":
    palabra = input("Palabra:")
    print(jerigonzo(palabra))