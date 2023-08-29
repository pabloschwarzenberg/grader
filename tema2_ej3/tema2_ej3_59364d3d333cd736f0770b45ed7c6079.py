def numero_perfecto(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    return suma_divisores == num

if __name__ == "__main__":
    num = int(input("Ingrese un nÃºmero: "))
    print(numero_perfecto(num))        