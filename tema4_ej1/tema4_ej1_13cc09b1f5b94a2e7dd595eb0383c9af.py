from random import randint
PalabrasSecretas = ["lepidoptero", "verdad", "adios", "gato", "perro", "programacion"]
Palabra = PalabrasSecretas[randint(0, len(PalabrasSecretas)- 1)]

def ocultar_letras(Palabra, Cantidad):
    Palabra_secreta = Palabra
    Contador = 0
    while (Cantidad > Contador):
        index = randint(0, len(Palabra_secreta) - 1)
        while (Palabra_secreta[index] == "_"):
            index = randint(0, len(Palabra_secreta) - 1)
        Palabra_secreta = str(Palabra_secreta[:index]) + "_" + str(Palabra_secreta[index + 1:])
        Contador += 1
    return Palabra_secreta

def revisar_letra(Palabra_secreta, Palabra, Letra):
    Counter = 0
    while (Counter < len(Palabra)):
        if (Letra == Palabra[Counter]):
            Palabra_secreta = str(Palabra_secreta[:Counter]) + str(Letra) + str(Palabra_secreta[Counter + 1:])
        Counter += 1
    if (Letra == Palabra):
        Palabra_secreta = Palabra
    print(Palabra_secreta)
    return Palabra_secreta