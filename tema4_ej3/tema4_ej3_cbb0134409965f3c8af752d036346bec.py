def jerigonzo(palabra):
for letra in palabra:
    if letra in "AEIOUaeiou":
        translado += letra
        translado += "p"
    translado += letra

print(translado)

if __name__=="__main__":
    palabra = input("Ingresa una palabra: ")
    print(translado)
    pass