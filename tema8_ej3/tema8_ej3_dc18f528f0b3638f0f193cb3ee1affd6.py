def estadisticas_frase(s):
    numero_palabras = 0

    total_caracteres = len(s)

    palabras = s.split()
    suma = 0
    for i in range(0,len(palabras)):
        palabra = ''.join(char for char in palabras[i] if char.isalnum())
        if(palabra):
            numero_palabras += 1
            suma += len(palabra)

    avg_largo_palabras = suma/numero_palabras

    numero_espacios = s.count(" ")

    caracteres_puntuacion = s.count(".")+s.count(",")+s.count(":")+s.count(";")
    
    return numero_palabras, total_caracteres, avg_largo_palabras, numero_espacios, caracteres_puntuacion

if __name__ == "__main__":
    print(estadisticas_frase("quelaaaaa, .:: pasa cava todo bien"))
         