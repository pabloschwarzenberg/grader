def buscarTodas(a,b):
    final=[]
    posicion=0
    for i in a:
        if i==b:
            final.append(posicion)
        posicion+=1
    string=""
    for i in final:
        string += str(i)+" "
    string = string[:-1]
    
    return(string)
