def numero_perfecto(a):
    suma_divisores_a =0
    ax = 1
    while ax < a:
        if a % ax == 0:
            suma_divisores_a+=ax
        else:
            pass
        ax += 1

    if suma_divisores_a==a:
        return True
    else:
        return False

if __name__=="__main__":
    n=int(input("Ingrese hasta que numero quiere operar: "))
    suma=0
    z=1
    while z<n:
        if numero_perfecto(z):
            suma+=z
        else:
            pass
        z+=1

    print(suma)
           