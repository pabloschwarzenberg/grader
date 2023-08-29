def buscarTodas(a,b):
    posiciones=[]
    i=0
    largo=len(a)
    for i in range(largo) :
        if a[i]==b:
            posiciones.append(i)
    final=" ".join(str(x) for x in posiciones)
    return final

if __name__ == "__main__":
    pass
           