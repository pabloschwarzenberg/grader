def jerigonzo (pal):
    cambio =""
    for letra in pal:
        if letra in "AEIOUaeiou":
            cambio += letra
            cambio +="p"
        cambio += letra
    return cambio

if __name__=="__main__":
    palabra= input("Ingresa una palabra: ")
    print(jerigonzo(pal))