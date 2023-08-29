# completa el código de la función
def suma_divisores(x):
    suma=0
    z=0
    if x%2==0:
        for i in range(1,x):
            if x%i==0:
                suma=suma+i
        return (suma,False)
    if x%2 !=0:
        for j in range(1,x):
            if x%j ==0:
                z= z+j
        return (z,True)
    else:
        return (suma,True)


if __name__ == "__main__":
    x=int(input("ingresa un numero:"))
    l=suma_divisores(x)
    print(l)