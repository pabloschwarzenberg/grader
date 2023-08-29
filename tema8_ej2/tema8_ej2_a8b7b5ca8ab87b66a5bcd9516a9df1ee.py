def buscarTodas(a,b):
    busqueda=""
    busqueda2=""
    for i in range(len(a)):
        if a[i]==b:
            if i<(len(a)-1):
                busqueda+=str(i)+ " "
                 
    return busqueda.strip()
        
    
    
    

if __name__ == "__main__":
    a=input("ingrese palabra:")
    b=input("ingrese a buscar:")
    print(buscarTodas(a,b))
    

    
    

if __name__ == "__main__":
    a=input("ingrese palabra:")
    b=input("ingrese a buscar:")
    print(buscarTodas(a,b))
           