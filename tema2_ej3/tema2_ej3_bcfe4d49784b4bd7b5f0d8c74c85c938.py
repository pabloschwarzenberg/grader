def numero_perfecto(num):
    suma_divisores = sum([divisor for divisor in range(1, num) if num % divisor == 0])
    return suma_divisores == num

if __name__ == "__main__":
    num = int(input("Ingresa un número: "))
    if numero_perfecto(num):
        print(num, "es un número perfecto")
    else:
        print(num, "no es un número perfecto")
