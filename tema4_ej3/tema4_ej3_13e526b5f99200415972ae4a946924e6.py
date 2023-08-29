def jerigonzo(Palabra):
    translado = ""
    for letra in Palabra:
        if letra in "AEIOUaeiou":
            translado +=letra
            translado +="p"
        translado += letra
    return translado      

if __name__ == "__main__":
    pass
         