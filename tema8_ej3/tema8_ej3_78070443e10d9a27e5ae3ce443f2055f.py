def estadisticas_frase(s):
    palabras = s.split(" ")
    total_letras = len(s) - s.count(" ")
    largo_promedio = total_letras/len(palabras)
    espacios = s.count(" ")
    numero_puntuacion = total_letras - len(s) - espacios
    return len(palabras), total_letras, largo_promedio, espacios, numero_puntuacion

if __name__ == "__main__":
    s = "El hombre imaginario vive en una mansión imaginaria rodeada de árboles imaginarios a la orilla de un río imaginario"
    print(estadisticas_frase(s))
         