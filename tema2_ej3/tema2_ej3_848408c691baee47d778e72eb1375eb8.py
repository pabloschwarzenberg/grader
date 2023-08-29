def numero_perfecto(a):
    sum1 = 0
    for i in range(1, a):
        if a % i == 0:
            sum1 = sum1 + i
    if sum1 == a:
        return True
    else:
        return False


if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
           