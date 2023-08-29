def numero_perfecto(a):
    suma_divisores=0
    for x in range(1, a):
        if a%x==0:
            suma_divisores=suma_divisores+x

    if suma_divisores==a:
        return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           