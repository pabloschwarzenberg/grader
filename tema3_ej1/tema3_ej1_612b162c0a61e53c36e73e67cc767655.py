def suma_divisores(a):
    contador=1
    suma=0
    if a!=1:
        while contador!=a:
            if a%contador==0:
                suma=suma+contador
                contador=contador+1
            else:
                contador=contador+1
            if contador==a-1:
                if suma==1:
                    return (suma,True)
                else:
                    return (suma,False)
    elif a==1:
        return (0,False)
    
         
if __name__ == "__main__":
    a=int(input("Ingrese a: "))
    print (suma_divisores(a))

    