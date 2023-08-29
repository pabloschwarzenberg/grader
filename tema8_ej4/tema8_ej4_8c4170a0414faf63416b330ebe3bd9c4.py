#ENTRADA

def rot13(u):
    cifrado = "abcdefghijklmnopqrstuvwxyz"

#PROCESAMIENTO

    cesar = cifrado [13:] + cifrado [:13]
    cifrado_cesar = lambda l: cesar [cifrado.find(l)] if cifrado.find (l) >-1 else c 
    
#SALIDA
    return''.join (cifrado_cesar (l) for l in u)