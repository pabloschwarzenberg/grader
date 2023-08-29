def numero_perfecto(a):
    d=1
    suma=0
    while d!=a:
        if a%d==0:
            suma=suma+d
        d=d+1
    if suma==a:
        return True
    else:
        return False

if __name__ == "__main__":
    a=eval(input("Ingrese su numero: "))
    if numero_perfecto(a):
        print("El numero {0} es perfecto".format(a))
    else:
        print("El numero {0} no es perfecto".format(a))