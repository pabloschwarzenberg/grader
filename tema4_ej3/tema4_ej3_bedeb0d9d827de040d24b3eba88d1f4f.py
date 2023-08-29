def jerigonzo(string):
    stringJerizongo = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            #print(letra)
            stringJerizongo = stringJerizongo + letra
            stringJerizongo = stringJerizongo + "p"
            stringJerizongo = stringJerizongo + letra
        else:
            stringJerizongo = stringJerizongo + letra

    return stringJerizongo


if __name__ == "__main__":
    var = jerigonzo("estamos programando")
    print(var)
    pass
