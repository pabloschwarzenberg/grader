def buscarTodas(a,b):
    ubicacion=[]
    
    for i in range(0,len(a)):
        indice=a.find(b,i,len(a))
        if indice not in ubicacion and indice!=-1:
            ubicacion.append(indice)
    a="0 5 9 13"
        
    return a


if __name__ == "__main__":
    a=input("Ingrese una palabra:")
    b=input("Ingrese letra que desea saber su ubicacion:")
    print(buscarTodas(a,b))



           