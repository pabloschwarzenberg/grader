#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    
    if palabra1 == palabra2:
        return '0D' 

    if len(palabra1) != len(palabra2):
        
        if len(palabra1) - len(palabra2) > 1 or len(palabra2) - len(palabra1) > 1:
            return '+1'
        
        if len(palabra1) - len(palabra2) == 1 or len(palabra2) - len(palabra1) == 1:
            pml = palabra1 if len(palabra1) > len(palabra2) else palabra2
            pmc = palabra1 if len(palabra1) < len(palabra2) else palabra2

            contador = 0
            for i in range(len(pml)):
                
                if pml[i] != pmc[i]:
                    contador += 1

                    pmc = list(pmc)
                    pmc.insert(i, pml[i])
                    pmc_ = ''

                    for j in pmc:
                        pmc_ += j
                    
                    if pmc_ == pml:
                        return 'IB'
                
                if contador > 1:
                    return '+1'


    if len(palabra1) == len(palabra2):
        distancia = 0
        indice_d = 0
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]:
                distancia += 1
                indice_d = i
        
        if distancia == 1:
            comparacion1 = palabra1[:indice_d] + palabra2[indice_d] + palabra1[indice_d+1:] == palabra2
            comparacion2 = palabra2[:indice_d] + palabra1[indice_d] + palabra2[indice_d+1:] == palabra1
            if comparacion1 or comparacion2:
                return '1S'

        else:
            return '+1'

if __name__=="__main__":
    pass
           