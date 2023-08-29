def buscarTodas(a,b):
    apariciones=[]
    while a.find(b)!=-1:
        apariciones.append(str(a.find(b)))
        a=a.replace(b," ",1)
    out=" ".join(apariciones)
    return out

if __name__ == "__main__":
    a=input("Ingrese una palabra: ")
    b=input("Ingrese el elemento que desea buscar: ")
    print (buscarTodas(a,b))
           