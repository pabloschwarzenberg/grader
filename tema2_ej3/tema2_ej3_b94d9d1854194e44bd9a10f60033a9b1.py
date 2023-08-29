def numero_perfecto(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma == num

if __name__ == "__main__":
    num = int(input("Ingresa un número: "))
    if numero_perfecto(num):
        print(num, "es un número perfecto.")
    else:
        print(num, "no es un número perfecto.")
   