import random

def ocultar_letras(palabra,cantidad):
    palabraComoLista = list(palabra)
    ocultas = 0
    while ocultas <= cantidad:
        lugar = random.randint(0,len(palabra)-1)
        if palabraComoLista[lugar] != "_":
            palabraComoLista[lugar] = "_"

        else:
            lugar = random.randint(0, len(palabra) - 1)
        ocultas += 1

    palabra= "".join(palabraComoLista)
    return palabra



def revisar_letra(palabra_secreta,palabra,letra):
    palabraOculta = list(palabra)
    lugarLetra = palabra_secreta.find(letra)
    contador = lugarLetra + 1
    while contador < (len(palabra_secreta)):
        if palabra_secreta[contador] == letra:
           palabraOculta[contador] = letra
           contador += 1
        else:
            contador += 1

    palabraOculta = "".join(palabraOculta)

    return palabraOculta