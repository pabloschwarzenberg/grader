def numero_perfecto(a):
    suma_divisores = sum([i for i in range(1, a) if a % i == 0])
    if suma_divisores == a:
        return True
    else:
        return False

if __name__ == "__main__":
    a = int(input("Ingrese un número: "))
    print(numero_perfecto(a))
