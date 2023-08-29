def numero_perfecto(a):
    Suma_de_los_divisores = 0
    for i in range(1, a):
        if a % i == 0:
            Suma_de_los_divisores += i

    if Suma_de_los_divisores==a:
        return True
    else:
        return False

if __name__=="__main__":
    while True:
        a=int(input("Ingrese a: "))
        print(numero_perfecto(a))