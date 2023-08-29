frase = input("ingrese su frase: ")
translado = ""
for letra in frase:
    if letra in "AEIOUaeiou":
        translado += letra
        translado += "p"
    translado += letra
print(translado)