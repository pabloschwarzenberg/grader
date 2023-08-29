def buscarTodas(a,b):
    salida=[]
    for i in range(0,len(a)):
        if a[i]==b:
            salida.append(i)
        str_1="".join(str(x) for x in salida)
    return str_1
    pass

if __name__ == "__main__":
    pass
           