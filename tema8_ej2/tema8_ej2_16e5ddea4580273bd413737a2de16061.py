def buscarTodas(a,b):
    lista=[]
    
    posiciones=""
    for i in range(0,len(a)):
        lista.append(a[i:i+1])
    for x in range(0,len(a)):
        if b==lista[x]:
            posiciones+=str(x)+" "
    posiciones_kai=posiciones[0:len(posiciones)-1]
    return posiciones_kai

if __name__ == "__main__":
    a=str(input("Ingrese la frase: "))
    b=str(input("Ingrese la letra: "))
    print(buscarTodas(a,b))       