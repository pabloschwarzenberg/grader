def buscarTodas(a,b):
    fin=""
    while True:
        posicion=a.find(b)
        print(posicion)
        if posicion==-1:
            print("lol")
            break
        a=a.replace(a[posicion],"1",1)
        print(a)
        fin=fin+str(posicion)+" "
        print(fin)
    fin=fin.strip()
    return fin