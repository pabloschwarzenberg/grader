def suma_divisores(n):
    suma = 0

    for i in range(1, n + 1):
        if n % i == 0:
            suma += i

    return suma

if __name__ == "__main__":
    n=int(input("ingrese numero:"))
    print(suma_divisores(n))
          
