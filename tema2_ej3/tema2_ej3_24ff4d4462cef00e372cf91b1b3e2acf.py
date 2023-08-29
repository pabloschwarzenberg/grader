def numero_perfecto(a):
    suma = 0
    for k in range(1,a):
        if a%k == 0:
            suma += k
    return suma==a

if __name__ == "__main__":
    a= int(input("Ingrese a: "))
    print(numero_perfecto(a))