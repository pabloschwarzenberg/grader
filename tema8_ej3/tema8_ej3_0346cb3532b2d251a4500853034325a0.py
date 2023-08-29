import re

def estadisticas_frase(frase):
    # Eliminar caracteres especiales
    frase_limpia = re.sub(r'[^\w\s]', '', frase)

    # Dividir la frase en palabras
    palabras = frase_limpia.split()

    # Calcular el número total de palabras
    total_palabras = len(palabras)

    # Calcular el número de palabras distintas
    palabras_distintas = set(palabras)
    total_palabras_distintas = len(palabras_distintas)

    # Calcular la longitud promedio de las palabras
    suma_longitudes = sum(len(palabra) for palabra in palabras)
    longitud_promedio = suma_longitudes / total_palabras

    # Crear el diccionario de estadísticas
    estadisticas = {
        'Total de palabras': total_palabras,
        'Palabras distintas': total_palabras_distintas,
        'Longitud promedio': longitud_promedio
    }

    return estadisticas

if __name__ == "__main__":
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

    resultado = estadisticas_frase(hombre_imaginario)
    for clave, valor in resultado.items():
        print(clave + ":", valor)

