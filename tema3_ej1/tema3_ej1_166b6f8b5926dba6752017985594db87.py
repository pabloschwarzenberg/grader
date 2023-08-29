# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    if suma == 1:
        resultado=(suma, bool(1))
    elif suma>1 or suma==0:
        resultado=(suma, bool(0))
    return(resultado)
if __name__ == "__main__": 
    a = int(input("Ingresa el número: "))
    print("La suma es de sus divisores es: ")
    print(suma_divisores(a))