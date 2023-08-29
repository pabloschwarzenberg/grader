def jerigonzo(string):
    vocales="aeiou"
    traduccion=""

    for letra in string:
        if letra in vocales:
            traduccion+=letra
            traduccion+="p"
        traduccion+=letra

    return traduccion