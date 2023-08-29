def buscarTodas(a,b):
    la=list(a)
    n=0
    indices=[]
    for i in la:
        if i==b:
            indices.append(str(n))
            indices.append(" ")
            n+=1
        else:
            n+=1
    l=indices.pop(-1)
    ind="".join(indices)
    return ind
            
        
            
        

if __name__ == "__main__":
    a=input("palabra:")
    b=input("buscar:")
    print(buscarTodas(a,b))