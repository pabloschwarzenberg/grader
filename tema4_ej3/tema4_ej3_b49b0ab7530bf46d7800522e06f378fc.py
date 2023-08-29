def jerigonzo(string):
    vocales=("aeiou")
    traduccion=""
    for letra in string:
        traduccion+=letra
        if letra.lower() in vocales:
            traduccion+="p"+letra
    return traduccion

if __name__ == "__main__":
    string=input("Ingrese la frase a traducir: ")
    print(jerigonzo(string))
    pass
         