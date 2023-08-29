def es_primo():
    num = int(input("Ingresa un número: "))
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
if es_primo():
    print("El número es primo.")
else:
    print("El número no es primo.")   