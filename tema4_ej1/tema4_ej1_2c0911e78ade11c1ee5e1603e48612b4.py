import random

lista = ["hola", "juguete", "gato", "jalea"]
opcion = random.choice(lista)
nueva_lista = list(opcion)
vidas = 7
palabra_jugador = ' '



def ocultar_letras(palabra,cantidad):
    
    nueva_lista = list()
    ocultar = random.choice(nueva_lista, cantidad)

    for i in range(1, len(nueva_lista)):
    
        palabra = nueva_lista.append('_' if i in ocultar else i)
    
    return palabra
    
def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
         