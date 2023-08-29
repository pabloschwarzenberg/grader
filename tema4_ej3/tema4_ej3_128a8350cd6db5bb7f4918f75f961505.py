a=int(input("ingresa una palabra: "))
palabra=a
translado= ""
for letra in palabra:
    if letra in "AEIOUaeiou":
        translado += letra
        translado += "p"
        
    translado += letra
print(translado)         