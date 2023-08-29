def contar_puntuacion(a):
    puntos = a.count(".")
    comas = a.count(",")
    guion = a.count("-")
    guion_bajo = a.count("_")
    exclamacion = a.count("!¡")
    pregunta = a.count("?¿")
    punto_coma = a.count(";")
    tres_puntos = a.count("…")
    puntos_juntos = [puntos,comas, guion, guion_bajo, exclamacion, pregunta, punto_coma, tres_puntos]
    total_puntos = sum(puntos_juntos)
    return total_puntos

def contar_espacios(a):
    espacios = a.count(" ")
    return espacios

def contar_palabras(separar_palabras):
    return len(separar_palabras)

def longitud_palabras(separar_palabras):
    longitudes = map(len, separar_palabras)
    longitudes = list(longitudes)
    prom_longitudes = sum(longitudes)/len(longitudes)
    return prom_longitudes

def separar_palabras(a):
    palabras = a.split()
    return palabras

def contar_caracteres(a):
    largo = len(a)
    return largo

def estadisticas_frase(a):
    palabras = contar_palabras(separar_palabras(a))
    caracteres = contar_caracteres(a) - contar_puntuacion(a)
    espacios = contar_espacios(a)
    puntuacion = contar_puntuacion(a)
    prom_longitud = longitud_palabras(separar_palabras(a))
    return palabras, caracteres, prom_longitud, espacios, puntuacion

if __name__ == "__main__":
    a = input("Ingrese el texto: ")
    print(estadisticas_frase(a))