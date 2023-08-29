def numero_perfecto(a):
    d=0
    for i in range(a):
        if (a%(i+1))==0:
            d=d+i+1
            continue
        else:
            continue
    d=d-a
    return a==d


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))


    print("dime un numero y sumo los nros perfectos desde 1 hasta tu nro")
    n=int(input("dime tu nro: "))
    k=0
    for i in range(n):
        if str(numero_perfecto(n))=="True":
            k=k+i
            print("loco")
        else:
            continue
    print("la suma es :"+str(k))