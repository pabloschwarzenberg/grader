#Suma de los N primeros números
 
while True:
    try:
        n=int(input("Digite el valor de n: "))

        if n>1:
            break
        else:
            print("Debe colocar un numero entero positivo")
    except ValueError:   
        print("Debe escribir un numero valido")  

    print(suma)  

suma= n*(n+1)/2
print(" la suma desde 1 hasta {n} es igual {suma}")


print(sum(range(1, n+1)))

     