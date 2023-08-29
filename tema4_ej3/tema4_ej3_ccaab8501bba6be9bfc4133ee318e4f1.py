def jerigonzo(string):
    vocales="aeiou"
    consonantes="bcdfghjklmnñpqrstvwxyz"
    palabra=""
    for letra in string:
        if letra in consonantes:
            palabra+=(letra)
        if letra in vocales:
            palabra+=(letra)
            palabra+=("p")
            palabra+=(letra)
        if letra==" ":
            palabra+=" "
    return palabra
if __name__ == "__main__":
    answer=input(": ")
    print(jerigonzo(answer))
    

