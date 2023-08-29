
def estadisticas_frase(frase):
    letras=0
    numero_palabras = len(frase.split())
    caracteres = len(frase)
    for i in frase:
        if i.isalpha():
            letras += 1
        else:
            pass
    letras = letras/numero_palabras
    espacios = frase.count(' ')
    caracteres_puntuacion = frase.count('.')
    return numero_palabras,caracteres,letras,espacios,caracteres_puntuacion
    
    
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         