import random as rn
def ocultar_letras(palabra, cantidad):
    cantidad_ocultada = 0
    while cantidad_ocultada < cantidad:
        indice = rn.randint(0, len(palabra)-1)

        letra_remplazada = palabra[indice]

        if letra_remplazada != '_':
            cantidad_letras = palabra.count(palabra[indice])
            
            if cantidad_ocultada + cantidad_letras <= cantidad:
                palabra = palabra.replace(letra_remplazada, '_')
                cantidad_ocultada += cantidad_letras
               
    
    return palabra
        

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = ''

    if letra not in palabra_secreta:
      
        return palabra

    elif letra in palabra_secreta:
        
        for i in range(len(palabra_secreta)):
            letra_secreta = palabra_secreta[i]

            if letra_secreta == letra:
                nueva_palabra += letra_secreta

            else:
                nueva_palabra += palabra[i]
            
    
    return nueva_palabra

