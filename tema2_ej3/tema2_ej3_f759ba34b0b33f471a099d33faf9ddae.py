def numero_perfecto(n):
    suma = 0

    for i in range(1, n):
        if n % i == 0:
            suma += i

    return suma == n



if __name__=="__main__":
    n=int(input("Ingrese un numero: "))
    print(numero_perfecto(n))
           