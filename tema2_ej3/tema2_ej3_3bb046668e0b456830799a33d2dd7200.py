def numero_perfecto(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i

    if suma == a:
        return True  # El número es perfecto
    else:
        return False  # El número no es perfecto


if __name__ == "__main__":
    a = int(input("Ingrese un número: "))
    print(numero_perfecto(a))
           