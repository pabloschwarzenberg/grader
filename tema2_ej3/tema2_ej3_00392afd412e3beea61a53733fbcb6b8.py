def numero_perfecto(a):
    t1 = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            print(i)
            t1.append(i)
    t2 = sum(t1) - a
    if t2 == a:
        return True

    if t2 != a:
        return False


if __name__ == "__main__":
    a1 = int(input("Ingrese a: "))
    print(numero_perfecto(a1))
