import random
palabras_secretas = ["agua","pedro","pablo","casa"]
numero_azar = random.randint(0,3)
palabra = palabras_secretas[numero_azar]

superior = len(palabra)
cantidad = random.randint(0,superior)
def ocultar_letras(palabra,cantidad):
    lista_palabra = list(palabra)
    
    i = 0
    largo_lista = len(lista_palabra) - 1
    while i < cantidad:
        posicion_ocultar = random.randint(0,largo_lista)
        lista_palabra[posicion_ocultar] = "-"
        i = i + 1
    return(lista_palabra)
        

