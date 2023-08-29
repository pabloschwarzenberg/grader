def buscarTodas(a,b):
    lista=[]
    cont=0
    for i in a:
        if i==b:
            cont=str(cont)
            lista.append(cont)
            cont=int(cont)
        cont=cont+1
    return lista

if __name__=="__main__":
    hola=input("Palabra: ")
    hola2=input("Letra a buscar: ")
    print("".join(buscarTodas(hola,hola2)))