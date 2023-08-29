def numero_perfecto(a):

    if a==1:
        return True

    else:
        contador=1
        suma=0

    while contador<a:
        if a%contador==0:
            suma=suma+contador

        contador=contador+1

    if suma==a:
        return True
    else:
        return False



if __name__ == '__main__':
    
    a=int(input("Ingrese a: "))

    i=1
    suma=0

    if a==1:
        suma=1
        print(suma)

    else:
        while i< a:
            if numero_perfecto(i)== True:
                suma=suma+i

            i=i+1

        print(suma)