def buscarTodas(a,b):
    posiciones=""
    for i in range(0,len(a)):
        if a[i]==b:
            posiciones+=str(i)+" "
        else:
            i=i+1
            
    lista=list(posiciones)
    sin_espacio=lista.pop(8)
    final="".join(lista)
    
    return final
        
  
    


    pass

if __name__ == "__main__":
    pass