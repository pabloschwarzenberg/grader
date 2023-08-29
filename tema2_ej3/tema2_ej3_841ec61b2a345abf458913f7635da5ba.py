def numero_perfecto(a):
    sumdivi = 0

    for i in range(1, a):
        if a % i == 0:
            sumdivi += i

    return sumdivi == a


if __name__ == "__main__":
    a = int(input("Ingrese un número: "))
    perfecto = numero_perfecto(a)

    if perfecto:
        print("True")
    else:
        print("False")
