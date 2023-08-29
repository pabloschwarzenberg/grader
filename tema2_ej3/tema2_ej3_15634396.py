def numero_perfecto(numero):
    qwerty=numero
    a=1
    c=0
    while a<qwerty:
        b=qwerty%a
        if b==0:
            c=c+a
            a=a+1
        else:
            c=c
            a=a+1
    if c==numero:
        return True
    else:
        return False
        


if __name__ == "__main__":

    print("Descubramos los numeros perfectos")
    a=int(input("Introduzca un numero: "))
    print(numero_perfecto(a))

    zx=0
    b=int(input("Introduzca un numero para encontrar la suma de numeros perfectos inferiores a este: "))
    poi=b
    while b>1:
        e=numero_perfecto(b)
        if e==True:
            print(b)
            zx=zx+b
            b=b-1
        if e==False:
            b=b-1
            zx=zx
    print("La suma de numeros perfectos menores o iguales a ",poi," es: ",zx)
           