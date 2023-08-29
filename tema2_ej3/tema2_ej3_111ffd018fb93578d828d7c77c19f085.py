def numero_perfecto(a):
    suma = 0

    for x in range(1,a):
        if a % x == 0:
            suma += x
    return suma == a

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))