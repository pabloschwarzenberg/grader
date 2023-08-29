def buscarTodas(a,b):
    indexes=''
    removed=0
    c=len(a)
    for i in range(c):
        index=a.find(b)
        a=list(a)
        if index==0:
            indexes+=str(removed)+' '
        a.pop(0)
        removed+=1
        a="".join(a)
    indexes=indexes[0:len(indexes)-1]
    return indexes

if __name__ == "__main__":
    parola=input("Ingrese dónde buscar: ")
    quelque=input("Ingrese qué buscar: ")
    indexes=buscarTodas(parola,quelque)
    print(indexes)
           