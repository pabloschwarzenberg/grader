import random

def ocultar_letras(palabra,cantidad):
    ocultar = 0
    palabral = list(palabra)
    while ocultar <= cantidad:
        posicion = random.randint(0, len(palabra) - 1)
        if palabral[posicion]!= "_":
            palabral[posicion]= "_"
        else:
            random.randint(0, len(palabra) - 1)
        ocultar+=1
    return "".join(palabral)
   
def revisar_letra(palabra_secreta,palabra,letra):
    palabral = list(palabra)
    posletra = palabra_secreta.find(letra)
    posfinal = posletra + 1 
    while posfinal < len(palabra_secreta):
        if palabra_secreta[posfinal] == letra:
            palabral[posfinal] = letra
            posfinal=posfinal+1
        else:
            posfinal=posfinal+1
    return "".join(palabral)
        
   
    

if __name__ == "__main__":
    pass
         