def ocultar_letras(palabra,cantidad):
    import random 
    
    n=0
    posiciones=[]
    while n<cantidad:
        pos=random.randint(0,len(palabra))
        if not pos in posiciones:
            posiciones.append(pos)
            n=n+1                  
    resultado=""
    for i in range(len(palabra)):
        if i in posiciones:
            resultado=resultado+"_"
        else:
            resultado=resultado+palabra[i]
    return resultado

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_salida=""
    for i in range(len(palabra_secreta)):

        if palabra_secreta[i]==letra:
            palabra_salida+=letra
        else:
            palabra_salida+=palabra[i]
           
    return palabra_salida
    
import random
palabras_secretas=["cancion","pelicula","paises","paralelepipedo","cine","circo","dinosaurio"]
palabra_secreta=random.choice(palabras_secretas)
cantidad= random.randint(1,len(palabra_secreta))
palabra=ocultar_letras(palabra_secreta,cantidad)
        