def buscarTodas(a,b):
    lista_a=[]
    contador=0
    lista_b=[]
    for i in a:
        lista_a.append(i)
    for i in a:
        if b==lista_a[lista_a.index(i)]:
            lista_b.append(lista_a.index(i))
            lista_a[lista_a.index(i)]=0
    lista_b=" ".join(str(x) for x in lista_b)
    return lista_b
            
        
        
    
    pass




if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres","t"))
    pass           