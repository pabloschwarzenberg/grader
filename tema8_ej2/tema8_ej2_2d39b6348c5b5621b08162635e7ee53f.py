def buscarTodas(a,b):
    lista = []
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)
    
    return lista

if __name__ == "__main__":       
    a=str(input("Ingrese a: "))
    b=str(input("Ingrese b: "))
    print (buscarTodas(a,b))
           