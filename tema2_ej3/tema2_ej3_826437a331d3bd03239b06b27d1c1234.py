def numero_perfecto(a):
    divisor = []
    for i in range(1, a):
        if a % i == 0:
            divisor.append(i)
    divisores = sum(divisor)
    if divisores == a:
        return True
    else:
        return False


if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
           