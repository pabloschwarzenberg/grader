def buscarTodas(a,b):
    lista =[]
    j=" "
    for x in range(len(a)):
        if a[x]==b:
            lista.append(str(x))
            l=j.join(lista)
        if len(lista)==0:
          return "no existe"
    
    return l  
     
          
if __name__ == "__main__":
    pass
           