def ocultar_letras(palabra, cantidad):
    cantidad_ocultada = 0
    import random as r
    while cantidad_ocultada < cantidad:
        indice = r.randint(0, len(palabra)-1)

        letra_remplazada = palabra[indice]

        if letra_remplazada != '_':
            cantidad_letras = palabra.count(palabra[indice])
            
            if cantidad_ocultada + cantidad_letras <= cantidad:
                palabra = palabra.replace(letra_remplazada, '_')
                cantidad_ocultada += cantidad_letras
                #print('Quitando letra', letra_remplazada, palabra.count(palabra[indice]))
    
    return palabra
        

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = ''

    if letra not in palabra_secreta:
        #print('La palabra secreta no tiene esa letra')
        return palabra

    elif letra in palabra_secreta:
        
        for i in range(len(palabra_secreta)):
            letra_secreta = palabra_secreta[i]

            if letra_secreta == letra:
                nueva_palabra += letra_secreta

            else:
                nueva_palabra += palabra[i]
            #print(nueva_palabra, letra_secreta ,letra)
    
    return nueva_palabra

if __name__ == "__main__":
    pass
         