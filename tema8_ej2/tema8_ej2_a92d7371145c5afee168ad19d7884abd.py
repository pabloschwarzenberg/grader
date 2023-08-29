def buscarTodas(a,b):
    lista=[]
    j=0
    w=0
    for i in a:    
        if b==i:
            if w != 0:
                lista.append(" ")
            w=w+1
            lista.append(str(j))
            
        j=j+1
    
    lista_final="".join(lista)
    
    return lista_final

if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres","t"))
    
    