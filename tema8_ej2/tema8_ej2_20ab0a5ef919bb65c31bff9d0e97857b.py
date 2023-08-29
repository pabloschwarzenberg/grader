#Función buscarTodas
def buscarTodas(a,b):
    pal=list(a)
    resultado=""
    for i in range(len(a)):
        if(pal[i]==b):
            resultado=resultado+str(i)+" "

    return resultado[:-1]