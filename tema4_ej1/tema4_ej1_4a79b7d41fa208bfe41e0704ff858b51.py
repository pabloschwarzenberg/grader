import random

def ocultar_letras(parametro, cantidad):

    lista = list(parametro)

    counter = 0
    while counter < cantidad:
        for i in range(len(lista)):
            # de forma random elijo si este indice lo reemplazo o no
            if random.random() > 0.5:
                if lista[i] != "_":
                    lista[i]="_"
                    counter += 1
                    if (counter >= cantidad):
                        break
    
    lista = "".join(lista)
    
    return lista

def revisar_letra(parametro, palabra_secreta, letra):

    # usuario intento adivinar toda la palabra
    if len(letra) == 1:
        
        # cambiar strings a listas
        parametro = list(parametro)
        palabra_secreta = list(palabra_secreta)
        
        # iterar por todos los caracteres de la palabra
        for i in range(len(parametro)):
            # si la letra existe en la palabra, reemplazamos "_" con ella
            if letra == parametro[i]:
                palabra_secreta[i] = letra
            
        # convertir de vuelta a string
        palabra_secreta = "".join(palabra_secreta)    
    
    return palabra_secreta

if __name__ == "__main__":
    lista_palabras = ["hola", "elias", "rose", "eefaa"]
    i = random.randint(0, len(lista_palabras) - 1)
    parametro = lista_palabras[i]
    cantidad = random.randint(1, len(parametro) - 1)
    
    # obtener palabra oculta
    palabra_oculta = ocultar_letras(parametro, cantidad)

    # jugar hasta que se acaben los intentos o palabra sea descubierta
    for i in range(7):
        letra = raw_input("Ingrese un letra o adivine la palabra completa. La palabra es: "+str(palabra_oculta)+" \n")
        
        palabra_oculta = revisar_letra(parametro, palabra_oculta, letra)
    
        # si no quedan "_" en la palabra, entonces hemos adividinado correctamente
        if "_" not in list(palabra_oculta):
            break
