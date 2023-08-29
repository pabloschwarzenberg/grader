# completa el código de la función
def suma_divisores():
    numero=int(input("Por favor, ingrese un numero entero mayor a 0: "))

    if numero==0 or numero<0:
        print("Ingrese un numero mayor a 0")
    elif numero>0:
        print("Divisores de",numero,": ", end="")
        for i in range (1,numero):
            if numero%i==0:
                print(i,",",end="")


        suma=0
        for i in range(1,numero):
            if numero%i==0:
                suma=suma+i

        print("\nSuma de sus divisores: ",suma)
        if suma==1:
            print("Primo")
        elif suma!=1:
            print("No Primo")


suma_divisores()