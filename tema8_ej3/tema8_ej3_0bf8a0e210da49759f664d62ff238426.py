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

    especiales = '!.,:;-_?¡¿#$%&/|/()='

    lista_palabras = frase.split()
    
    # Quitando los signos de puntuacíon de las palabras separadas
    
    caracteres_esp = 0
    
    indice = 0
    for palabra in lista_palabras:
        np = ''
        for caracter in palabra:
            if caracter in especiales:
                caracteres_esp += 1
                continue

            else:
                np += caracter

        lista_palabras[indice] = np
        indice += 1
    
    espacios_blanco = 0

    # Contando espacios en blanco
    for letra in frase:
        if letra == ' ':
            espacios_blanco += 1

    num_palabras = len(lista_palabras)
    caracteres_totales = len(frase)

    total = 0

    for palabra in lista_palabras:
        total += len(palabra)
    
    largo_promedio = total / len(lista_palabras)

    return (num_palabras, caracteres_totales, largo_promedio, espacios_blanco, caracteres_esp)
    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         