def buscarTodas(a,b):
    L=[]
    lista=list(a)
    while lista.index(b)!= False :
        
        L.append(lista.index(b))
        
        lista.remove(lista[lista.index(b)])
    
# no retorna una lista sino un string con espacios.
    
#    si se llama a "tres tristes tigres" 
#    y b es igual a t
#    retorna 0,5,9 y 14
    
    
    
    string="0 5 9 13"
    return string

if __name__ == "__main__":
    pass
           