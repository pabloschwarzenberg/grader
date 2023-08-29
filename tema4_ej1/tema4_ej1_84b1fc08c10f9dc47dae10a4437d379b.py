import random

def ocultar_letras(palabra,cantidad):
    """r = random.randint(0, len(palabra)-1)
    palabra = palabra[r]"""
    letras = []
    x = 0
    
    for i in range(len(palabra)):
        letras.append(x)
        x += 1
   
    for i in range(cantidad):
        x = random.randint(0, len(letras)-1)
        palabra = palabra.replace(palabra[letras[x]], "_", 1)
        letras.pop(x)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    if letra == palabra_secreta:
        return palabra_secreta
    else:
        if letra in palabra_secreta:
            x = palabra.find("_")
            if palabra_secreta[x] == letra:
                palabra.replace("_", letra)
            
    return palabra

if __name__ == "__main__":
    pass
         