def jerigonzo(palabra):
    contenedor = ""
    
    for letra in palabra:
        if letra in "AEIOU" or letra in "aeiou":
            contenedor += letra
            contenedor += "p"
        contenedor += letra
    return contenedor       
if __name__ == "__main__":
    palabra = input("->")
    jerigonzo(palabra)
    print(jerigonzo(palabra))
