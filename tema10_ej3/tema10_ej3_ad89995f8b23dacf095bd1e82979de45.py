if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
    ##sopa de letras
if __name__ =="__main__":
    f=open("sopa.txt","r")
    lista=f.readlines()

    primera_linea=lista[0].rstrip("\n")
    n=""
    m=""

    aux=0

    for i in primera_linea:
        if i =="":
            aux=1
        if aux==0:
            n=n+1
        elif aux==1:
            m=m+1
    n=int(n)
    m=int(m)
    matriz=[]

    for i in range(n):
        linea=lista[i+1].rstrip("\n")
        if(len(linea)==m):
            matriz.append(linea)
        else:
            matriz.append(linea[0:m])
    print(matriz)
    cantidad_de_palabras=int(lista[n+1].rstrip("\n"))

    verificador=0
    
    for i in range(cantidad_de_palabras):
        verificador=0
        palabra= lista[i+n+1+1].restrip("\n")
        print(palabra)
        for j in matriz:
            if j.find(palabra)==1 or j.find(palabra)==0:
                verificador=1
                print("encontrado")
                break
        if verificador==0:
            for j in matriz:
                if j[::-1].find(palabra)==1 or j[::-1].find(palabra)==0:
                    verificador=1
                    print(j.j[::-1],palabra)
                    print("encontrado")
                    break
        if verificador==0:
            for k in range(m):
                palabra_construida=""
                for i in range(n):
                    palabra_construida=palabra_construida + matriz[n1][k]
                print(palabra_construida)
                if palabra_contruida.find(palabra)==1 or palabra_construida.find(palabra)==0:
                 verificador=1
                print("Encontrado")
                break
            if palabra_contruida.find(palabra)==1 or palabra_construida.find(palabra)==0:
                verificador=1
                print("encontrado")
                break
            if verificador==0:
                print("No Encontrado")



           