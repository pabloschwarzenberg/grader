def ocultar_letras(palabra,cantidad):
    import random
    palabra=list(palabra)
    largo=len(palabra)
    i=0
    while i<cantidad:
        posicion=random.randint(0,(largo-1))
        palabra[posicion]="_"
        i=i+1
    palabra="".join(palabra)
    return palabra 
    
def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta=list(palabra_secreta)
    palabra=list(palabra)
    largo=len(palabra)
    i=0
    while i<largo:
        if letra==palabra_secreta[i]:
            palabra[i]=letra
        i=i+1
    palabra="".join(palabra)
    return palabra

if __name__ == "__main__":
    pass
         