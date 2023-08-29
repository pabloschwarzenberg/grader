import random

def imprimir(listaActual):
    print(' '.join(listaActual))

max_intentos = 5
listaPalabras = ['amor', 'boda', 'adivinanza', 'amarillo', 'silla', 
'telefono', 'ballena', 'radio', 'automovil']

palabraEscogida = random.choice(listaPalabras)
revisar_letra = list(palabraEscogida)
longLista = len(revisar_letra) # longitud de la palabra
ocultar_letras = ['_' for _ in range(longLista)] # Lista de guiones bajos [_, _, _, ...]

imprimir(ocultar_letras)
ganador = False
contador = 0
while max_intentos > 0:
    letra = input(f"Intentos [{max_intentos}] - Introduce una letra: ")
    acierto = False
    for i in range(longLista):
        if revisar_letra[i] == letra:
            ocultar_letras[i] = letra # reemplaza _ por la letra actual
            contador += 1
            acierto = True
    if not acierto: # La letra no está
        max_intentos -= 1
    imprimir(ocultar_letras)
    if contador == longLista: # Se adivinaron todas la letras
        ganador = True
        break
        
if ganador:
    print(" *** Ganaste el juego ***")
else:
    print(f"[!] Perdiste el juego, la palabra era: {palabraEscogida}")