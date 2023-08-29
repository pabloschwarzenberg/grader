def numero_perfecto(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma == num

if __name__ == '__main__':
    num = int(input("Introduce un número: "))
    es_perfecto = numero_perfecto(num)
    if es_perfecto:
        print(f"{num} es un número perfecto.")
    else:
        print(f"{num} no es un número perfecto.")
           