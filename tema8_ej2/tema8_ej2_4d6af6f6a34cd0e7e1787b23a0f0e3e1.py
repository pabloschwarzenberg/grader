def buscarTodas(a,b):
    contador=""
    count=0
    while count>=0:
        count=a.find(b)
        if count==-1:
            break
        a=a.replace(b,"x",1)
        c=str(count)
        contador=contador+" "+c
        contador=contador.strip()
    return(contador)
    pass


if __name__ == "__main__":
    pass
           