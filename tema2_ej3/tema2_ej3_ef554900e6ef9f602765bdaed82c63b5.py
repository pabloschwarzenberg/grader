def numero_perfecto(a):
    n = 1
    divisores = []
    suma = 0
    while n < a:
        if a % n == 0:
            divisores.append(n)
        n = n + 1
    for i in divisores:
        suma = suma + i
    if suma == a:
        return True
    else:
        return False

if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))