def numero_perfecto(a):
    suma = 0
    for numero in range(1, a + 1):
        if (a % numero) == 0:
            suma = suma + numero
    suma = suma - a
    if suma == a:
        return True
    else:
        return False


if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))