def numero_perfecto(a):
    suma = sum(i for i in range(1, a) if a % i == 0)
    return suma == a

if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    if numero_perfecto(a):
        print(a, "es un número perfecto")
    else:
        print(a, "no es un número perfecto")