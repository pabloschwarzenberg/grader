palabra=input("Ingresa una palabra: ")
traslado = ""
for letra in palabra:
    if letra in "AEIOUaeiou":
        traslado += letra
        traslado += "p"
    traslado += letra
print(traslado)