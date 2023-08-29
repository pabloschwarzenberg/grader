import random

def ocultar_letras(palabra, cantidad):
    
    palabra = list(palabra)
    done = False
    
    while not done:
        
        idx = random.randint(0, len(palabra) - 1)

        if palabra[idx] != '_':
            palabra[idx] = '_'
            cantidad -= 1

        if cantidad == 0:
            done = True

    return ''.join(palabra)

def revisar_letra(palabra_secreta, palabra, letra):
    
    palabra = list(palabra)
    
    for idx in range(len(palabra_secreta)):
        if palabra[idx] == '_':
            if palabra_secreta[idx] == letra:
                palabra[idx] = letra 
                
                return ''.join(palabra)
    
    return palabra