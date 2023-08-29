def buscarTodas(a,b):
    lista_abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lista_frase=list(a)
    retorno=[]
    for i in range(0,len(lista_frase)):
        x=lista_frase[i]
        if x==b:
            i=str(i)
            
            retorno.append(i+" ")
    retorno = "".join(retorno)
    largo = len(retorno)
    retorno = retorno[0:largo-1]
    print(retorno)
    
    return(retorno)

if __name__ == "__main__":
    pass
           