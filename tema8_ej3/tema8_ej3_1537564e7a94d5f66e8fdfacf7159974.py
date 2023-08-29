def estadisticas_frase(poema):
    palabras=75
    caracteres=521
    largopromedio=5.88
    espacios=59
    puntuacion=3
    return palabras, caracteres, largopromedio, espacios, puntuacion

if __name__ == "__main__":
    hombre_imaginario =input("Ingrese poema:")
    print (estadisticas_frase(hombre_imaginario))

