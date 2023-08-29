import random

def ocultar_letras(palabra,cantidad):
    largo = len(palabra)
    i = 1
    while i <= cantidad:
        kk = True
        while kk == True:

            posicion = random.randint(1,largo - 1)
           
            if palabra[posicion - 1] != "_":
                kk = False
           
             
        texto = palabra[0:posicion - 1] + "_" 
        texto2 = palabra[len(texto): largo-1]
        palabra = texto + texto2
        i = i+1
    
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):

    largo = len(palabra_secreta)
    i = 0
    while i <= largo - 1:

        if palabra_secreta[i]==letra:
             texto = palabra[0:i] + letra 
             texto2 = palabra[len(texto): largo-1]
             palabra = texto + texto2

            
        i = i+1
    
    return palabra