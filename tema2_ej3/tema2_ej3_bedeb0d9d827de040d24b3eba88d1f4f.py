def numero_perfecto(a):
    sumaDivisores = 0
    for x in range(1,a):
        if a % x == 0 and x != a:
            sumaDivisores = sumaDivisores + x
    if sumaDivisores == a:
        return True
    else:
        return False


if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
