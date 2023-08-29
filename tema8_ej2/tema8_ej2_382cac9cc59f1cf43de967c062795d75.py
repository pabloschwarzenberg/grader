def buscarTodas(a,b):
    indice=0
    c=[]
    while indice<len(a):
        indice_letra=a[indice]
        if indice_letra==b:
            c.append(str(indice))
        indice+=1
    return " ".join(c)


if __name__ == "__main__":
    pass
           