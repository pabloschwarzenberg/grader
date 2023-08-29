
def genoma(palabra):

    palabra=palabra.lower()

    for i in range(len(palabra)):

        if ("a"==palabra[i] or "c"==palabra[i])or("t"==palabra[i] or "g"==palabra[i]):

            continue

        else:

            return "Secuencia incorrecta"


    return "Secuencia correcta"


e=input("Inserte el código:")

r=genoma(e)

print(r)
