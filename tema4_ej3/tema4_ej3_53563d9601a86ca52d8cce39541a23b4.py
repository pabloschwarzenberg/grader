def jerigonzo(palabra):
    traducir=""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            traducir += letra
            traducir += "p"
        traducir += letra
    return traducir

if __name__ == "__main__":
    palabra = input("ingresa una palabra: ")
    print(jerigonzo(palabra))
    pass