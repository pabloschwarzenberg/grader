def buscarTodas(a,b):
    d=[]
    al=list(a)
    for i in range(0,len(al)-1):
        if(al[i]==b):
            i=str(i)
            d.append(i)
            d.append(" ")
    if(i==len(al)):
        if(al[i]==b):
            i=str(i)
            d.append(i)
    e="".join(d)   
    return(e)
        
if __name__ == "__main__":
    a=input("string 1:")
    b=input("string 2:")
    print(buscarTodas(a,b))