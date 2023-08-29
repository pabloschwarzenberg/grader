vocales=["a","e","i","o","u"]

def jerigonzo(frase):
    p=" "
    newfrase=[]
    newpalabra=""
    palabras=frase.split()
    for palabra in palabras:
        for letra in palabra:
            if (letra in vocales)==False:
                newpalabra+=letra
            if (letra in vocales)==True:
                newpalabra=newpalabra+letra+"p"+letra
        newfrase.append(newpalabra)
        newpalabra=""
    return (p.join(newfrase))

if __name__ == "__main__":
    cosa=input("Ingrese frase: ")
    print(jerigonzo(cosa))