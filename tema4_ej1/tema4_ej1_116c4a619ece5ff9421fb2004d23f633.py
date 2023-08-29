from random import randint

def revisar_letra(palabra_secreta,palabra,letra):
    posiciones = [lista for lista, x in enumerate(palabra_secreta) if x==letra]
    for i in posiciones: 
       palabra = palabra[:i] + letra + palabra[i+1:]       
    return palabra
    
def ocultar_letras(palabra,cantidad):
    x_lista = []
    for i in range(cantidad):  
        while True:
            x = randint(0, cantidad)
            if x not in x_lista:
                break
        x_lista.append(x)
        palabra = palabra[:x] + "_" + palabra[x+1:]
    return palabra