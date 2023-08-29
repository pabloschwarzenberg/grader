#Juego adivina mi número
secreto = 6
numero = 0#Le das cualquier valor distinto al número secreto.
cont = 0
while numero != secreto and cont <5:
    numero = int(input("Ingresa un número: "))
    if numero > secreto:
        print("mi número es menor")
        cont = cont+1
    if numero < secreto:
        print("mi número es mayor")
        cont = cont+1
    if cont ==5:
        print("No adivinaste, mi número era", secreto)
    elif numero == secreto:
        print("Adivinaste, mi número era", secreto)