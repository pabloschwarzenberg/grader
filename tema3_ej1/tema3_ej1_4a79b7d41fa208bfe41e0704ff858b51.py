def suma_divisores(n):
    suma = 0
    for i in range(1,n):
        if (n%i==0):            
            suma += i
    if suma==1:
        return (suma, True)
    else:
        return (suma, False)

if __name__ == "__main__":
    n=int(input("Ingrese un numero: "))
    suma_divisores(n)