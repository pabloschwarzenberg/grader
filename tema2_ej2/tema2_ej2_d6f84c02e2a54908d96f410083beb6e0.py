def amigos(n,n2):
    i=1
    cont=0
    lista=[]
    while i<=n:
        if n%i==0:
            n1=i
            cont=cont+1
            lista.append(i)
        i=i+1
    suma=0
    for i in lista:
        suma=suma+i
    if (suma-n1)==n2:
        return True
    return False

if __name__=="__main__":
    numero=int(input("numero 1: "))
    numero2=int(input("numero 2: "))
    amigos(numero,numero2)
    amigos(numero2,numero)

    if (amigos(numero,numero2)==True) and (amigos(numero2,numero)==True ):
        print(True)
    else:
        print(False)