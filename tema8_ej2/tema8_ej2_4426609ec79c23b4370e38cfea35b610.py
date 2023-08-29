def buscarTodas(a,b):

    i=0
    texto=""
    semaforo = False

    for c in a:
        if c == b:
            if semaforo == False:

                texto = str(i)
            else:
                texto = texto + " " + str(i)
            semaforo = True
            
            
        i = i + 1
       

    return texto
def buscarTodas(a,b):

    i=0
    texto=""
    semaforo = False

    for c in a:
        if c == b:
            if semaforo == False:

                texto = str(i)
            else:
                texto = texto + " " + str(i)
            semaforo = True
            
            
        i = i + 1
       

    return texto