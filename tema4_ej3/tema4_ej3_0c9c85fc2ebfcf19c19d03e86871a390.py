def jerigonzo(string):
    traslado =""

    for letra in string:
        if letra in "aeiou":
            traslado+=letra
            traslado+="p"
        traslado+=letra

    return traslado


if __name__ == "__main__":
    palabra= input("Ingrese palabra: ")
    print(jerigonzo(palabra))

    pass
