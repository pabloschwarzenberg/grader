def buscarTodas(a,b):
    lista=[]
    cont = 0
    for letra in a:
        if letra==b:
            lista.append(str(cont))
        cont +=1
    b=" ".join(lista)
    return b
if __name__ == "__main__":
    pass
           