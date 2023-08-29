def buscarTodas(a,b):
    index=[]
    lugar=0
    for i in a:
        if i==b:
            index.append(lugar)
        lugar+=1
    string=""
    for i in index:
        string += str(i)+" "
    string = string[:-1]
    
    return(string)