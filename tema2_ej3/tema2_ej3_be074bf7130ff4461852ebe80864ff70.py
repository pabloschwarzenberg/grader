def numero_perfecto(k):
    #se determinan los divisores del numero
    #sin tomar en cuenta el mismo numero
    #su suman los divisores
    sd = 0 #sumador de divisores
    for i in range(1,k):
        if(k%i==0): # i es divisor del numero
            sd = sd + i
    #se compara con el numero
    if sd==k:
        return True
    else:
        return False
           