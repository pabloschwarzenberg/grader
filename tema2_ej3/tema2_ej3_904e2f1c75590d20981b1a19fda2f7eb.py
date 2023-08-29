def numero_perfecto(a):
    return False
suma = 0

if __name__ == "__main__":
    a = int(input("Ingrese a: "))

    for i in range(1, a):
        if a % 1 == 0:
            suma += 1

    print(numero_perfecto(a))
