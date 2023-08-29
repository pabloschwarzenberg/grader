def buscarTodas(a,b):
    L = []
    s = " "
    
    for j in range(len(a)):
        if(a[j] == b):
            L.append(str(j))
            y = s.join(L)
    if(len(L)==0):
        return "ERROR: No existe lo que acaba de colocar"
 
    return y

if __name__ == "__main__":
    pass
           