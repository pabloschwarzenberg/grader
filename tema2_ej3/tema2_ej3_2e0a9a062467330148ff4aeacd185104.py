def numero_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n
if __name__ == "__main__":
    print(numero_perfecto(6)) # True
    print(numero_perfecto(28)) # True
    print(numero_perfecto(12)) # False

           