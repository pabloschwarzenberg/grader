palabra = input("ingresa una palabra: ")
traduccion = ""

for letra in palabra:
    if letra in "AEIOUaeiou":
        traduccion += letra
        traduccion += "p"
    traduccion += letra

print(traduccion)