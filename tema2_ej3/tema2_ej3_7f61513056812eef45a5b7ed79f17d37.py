def numero_perfecto(a):
    contador=1
    suma=0
    while contador!=a:
        if a%contador==0:
            suma=suma+contador
        contador=contador+1
    if suma==a:
        return True
    else:
        return False
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    if numero_perfecto(numero):
        print("El numero {0} es perfecto".format(a))
    else:
        print("El numero {0} no es perfecto".format(a))
    


    

    