def buscarTodas(a,b):
    lista=[]
    for i in range(len(a)):
        if a[i]==b:
            lista.append(str(i))
    
    imprime=" ".join(lista)
    
    return imprime

if __name__ == "__main__":
    a=input('ingrese palabra:')
    b=input('ingrese lo que quiere buscar:')
    print(buscarTodas(a,b))           