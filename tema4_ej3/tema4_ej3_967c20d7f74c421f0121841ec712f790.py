def  jerigonzo(palabra):
 translado = ""
 for letra in palabra:
    if letra in "AEIOUaeiou":
        translado += letra
        translado += "p"
    translado += letra
 return translado