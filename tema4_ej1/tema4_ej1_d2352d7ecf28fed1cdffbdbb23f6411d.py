import random
letras_ocultas=[]
def ocultar_letras(palabra,cantidad):
    posicion_letra_anterior = ""
    for i in range(cantidad):
        posicion_letra = random.randint(0, len(palabra) - 1)
        if posicion_letra != posicion_letra_anterior:
            posicion = posicion_letra
            letra = palabra[posicion_letra]
            letra_posicion = [letra, posicion]
            palabra = list(palabra)
            palabra[posicion] = "_"
            palabra = "".join(palabra)
        posicion_letra2 = posicion_letra
        
    return palabra

def revisar_letra(palabra_secreta,palabra_borrador,letra):
    cantidad = palabra_secreta.count(letra)
    posiciones_secreta = []
    palabra_borrador = list(palabra_borrador)
    palabra_secreta = list(palabra_secreta)
    for i in range(len(palabra_secreta)):
        if letra == palabra_secreta[i]:
            posiciones_secreta.append(i)
        else:
            continue
    posiciones = []
    for i in range(len(palabra_borrador)):
        if letra == palabra_borrador[i]:
            posiciones.append(i)
        else:
            continue
    while len(posiciones_secreta) > len(posiciones):
        posiciones.append("-")
    contador_posicion_lista = 0
    for i in range(len(posiciones_secreta)):
        if posiciones[i] != posiciones_secreta[i]:
            palabra_borrador.pop(int(posiciones_secreta[i]))
            palabra_borrador.insert(int(posiciones_secreta[i]), letra)
            posiciones.insert(contador_posicion_lista, posiciones_secreta[contador_posicion_lista])
        else:
            contador_posicion_lista += 1
    palabra_borrador="".join(palabra_borrador)
    return palabra_borrador
    

if __name__ == "__main__":
    pass
         