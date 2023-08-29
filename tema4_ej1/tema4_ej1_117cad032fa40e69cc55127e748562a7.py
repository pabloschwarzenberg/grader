import random
def buscarPalabraAleat(listaPalabras):
    # Esta funcion nos devolvera una palabra elegida aleatoriamente.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]