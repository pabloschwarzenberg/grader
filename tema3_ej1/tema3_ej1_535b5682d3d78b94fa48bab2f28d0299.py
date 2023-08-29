def suma_divisores(var):
    num=0
    for i in range(1,var):
        if var % i == 0:
            num += i
    if num == 1:
        return (num,True)
    else:
        return (num,False)
if __name__ == "__main__":
    base = int(input("Ingrese el numero a calcular: "))
    print("La suma es: ",suma_divisores(base))


           