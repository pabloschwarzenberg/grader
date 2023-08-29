def buscarTodas(a,b):
    lista=[]
    cont=0
    for letra in a:
        if letra==str(b):
            lista.append(cont)
        cont+=1
    s=""
    for numero in lista:
        s=s+str(numero)+" "
    s=s.rstrip(" ")
    return s
            

if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres","t"))
    pass


           