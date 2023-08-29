import random
from random import*
palabras = ["manzana", "caballo", "oso"]

def palabra_al_azar(palabras):

    palabra = list(choice(palabras))
    return palabra

a = palabra_al_azar(palabras)
print(a)
palabra_al_azar


