def buscarTodas(a,b):
    list=[]
    for i in range(len(a)):
        if a[i]==b:
            list.append(str(i))
            
    
    return " ".join(list)

if __name__ == "__main__":
    a=input("Ingrese un texto: ")
    b=input("Ingrese la letra a buscar en la plabra anterios: ")
    print(buscarTodas(a,b))
           