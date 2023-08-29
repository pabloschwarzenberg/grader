def buscarTodas(a,b):
    cadenalis=list(a)
    nveces=a.count(b)
    final=(len(a))
    lista_final=[ ]
    cont=0
    inicio=0
    while cont<nveces:
        indice=cadenalis.index(b, inicio)     
        lista_final.append(str(indice))
        inicio=indice+1
        cont+=1
        if ValueError:
            continue        
    impfin=" ".join(lista_final)
    return impfin

if __name__ == "__main__":
    a=str(input("ingrese un string a: "))
    b=str(input("ingrese un string b: "))
    print(buscarTodas(a,b))