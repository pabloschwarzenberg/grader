def jerigonzo(palabra):
    translado=""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            translado+=letra
            translado+="p"
        translado+=letra
    return translado

if __name__=="__main__":
    palabra= input("Ingresa una palabra: ")
    print(jerigonzo(palabra))