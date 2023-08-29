def numero_perfecto(a):
    numSum = 0
    for i in range(a):
        if i != 0 and a % i == 0:
            numSum += i
    if numSum == a:
        return True
    return False


if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
