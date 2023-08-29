def numero_perfecto(a):
    suma = 0
    for i in range(1,a//2+1):
        if a / i == a // i:
            suma += i
    if suma == a:
        return True
    return False


if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))