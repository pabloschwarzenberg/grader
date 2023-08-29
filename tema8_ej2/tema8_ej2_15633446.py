def buscarTodas(string, letra):
    lista=[]
    posicion=-1
    while posicion<len(string):
        posicion=string.find(letra,posicion+1)
        if(posicion==-1):
            break
        else:
            r=str(posicion)
            lista.append(r)
    " ".join(lista)
    return(lista)

if __name__ == "__main__":
    pass
           