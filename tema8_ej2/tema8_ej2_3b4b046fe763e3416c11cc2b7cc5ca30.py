def buscarTodas(a,b):
    pos_dinamica=0
    posf=[]
    for i in a:
        if i==b:
            posf.append(pos_dinamica)
        pos_dinamica+=1
    retorno=''
    for i in posf:
        retorno=retorno+' '+str(i)
    return retorno[1:]

if __name__ == "__main__":
    pass
           