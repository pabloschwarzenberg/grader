def suma_divisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    if suma == 1:
        return suma, True # es primo
    else:
        return suma, False # no es primo


if __name__ == "__main__":
    num1 = 10
    suma1, primo1 = suma_divisores(num1)
    print(f"La suma de los divisores de {num1} es {suma1}, y el número {num1} {'es primo' if primo1 else 'no es primo'}")

    num2 = 13
    suma2, primo2 = suma_divisores(num2)
    print(f"La suma de los divisores de {num2} es {suma2}, y el número {num2} {'es primo' if primo2 else 'no es primo'}"

           