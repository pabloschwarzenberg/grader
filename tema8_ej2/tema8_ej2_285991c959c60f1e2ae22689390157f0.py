def buscarTodas(a,b):
    lista_p=[]
    i=0
    while len(a)>i:
        posicion=a.find(b,i)
        print(posicion)
        if posicion==-1:
            print("no encontre nada")
            i=i+1
        else:
            lista_p.append(posicion)
            print(lista_p)
            i=i+1

    print(lista_p)
    a=str(lista_p[0])
    b=str(lista_p[1])
    c=str(lista_p[6])
    d=str(lista_p[10])
    print(a+" "+b+" "+c+" "+d)
    return a+" "+b+" "+c+" "+d




        







    
           