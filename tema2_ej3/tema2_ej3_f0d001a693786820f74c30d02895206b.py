def numero_perfecto(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    if suma_divisores == num:
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    if numero_perfecto(num):
        print(f"{num} es un número perfecto")
    else:
        print(f"{num} no es un número perfecto")