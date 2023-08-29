hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""


def estadisticas_frase(frase):
    
    w = ((frase.splitlines()))
    # print(w)

    # print(w.count(" "))
    frase_nueva = ""
    numero_palabras = 0
    letras_palabras = 0
    numero_espacios = 0
    numero_puntos = 0
    for i in w:
        numero_espacios += i.count(" ")
        numero_puntos += i.count(".")
        frase_nueva += " " + i
    # print(frase_nueva[2:])
    frase_nueva = frase_nueva[1:]
    caract = len(frase_nueva)
    numero_caracteres = len(frase_nueva)

    numero_palabras = len(frase_nueva.split(" ")) - (frase_nueva.split(" ")).count("")
    # print((frase_nueva.split(" ").count("")))
    for x in frase_nueva.split(" "):

        for z in x:
            letras_palabras += len(z)

    promedio = round((letras_palabras - numero_puntos) / numero_palabras, 2)
    return numero_palabras, caract, promedio, numero_espacios, numero_puntos


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario)) 
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
