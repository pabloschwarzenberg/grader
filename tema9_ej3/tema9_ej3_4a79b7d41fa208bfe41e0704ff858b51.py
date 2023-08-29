def decodificar(string):
    
    # separar string en lista
    tmp = string.split(",") 
    
    # convertir a letra
    for i in range(len(tmp)):
        tmp[i] = int(tmp[i],2)
        tmp[i] = chr(tmp[i])
    
    # juntar todas las letras
    tmp = "".join(tmp)

    return tmp