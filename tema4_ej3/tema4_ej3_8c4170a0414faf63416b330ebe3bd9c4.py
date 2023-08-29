#ENTRADA

def jerigonzo(up):
    transformador = []
    
    for vocales in up:
        for vocales in vocales:
            if vocales in "AEIOUaeiou":
            
#PROCESAMIENTO
                vocales = vocales + "p" + vocales
            transformador.append(vocales)

#SALIDA

    transformador = "".join(transformador)
    return transformador