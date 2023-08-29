def numero_perfecto(x):
    divisores = [1]
    for i in range(2, x +1):
        if x % i == 0:
            divisores.append(i)
    if (sum(divisores)-x) == x:
        return True
    if (sum(divisores)-x) != x:
        return False




if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))

           