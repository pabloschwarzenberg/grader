def buscarTodas (string, letra):
    posicion=0
    lista=[]
    for caracter in string:
        if caracter==letra:
            lista.append(posicion)
            posicion+=1
        else:
            posicion+=1
            continue
    lista = ' '.join(str(e) for e in lista)
    return lista

if __name__ == "__main__":
    pass
           