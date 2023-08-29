# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1,a):
        if a % i == 0:
            suma += i

    return suma
if __name__ == "__main__":
    numero = int(input("Ingrese un numero: "))
    suma = suma_divisores(numero)
    print(f"Suma divisores: {suma}")
    if suma == 1:
        print("El numero es primo")
    else:
        print("El numero no es primo")