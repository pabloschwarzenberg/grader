def numero_perfecto(var):
    num=0
    for i in range(1,var):
        if var % i == 0:
            num += i
    if num == var:
        print(num)
        return True
    else:
        print(num)
        return False
if __name__ == "_main_":
    base = int(input("Ingrese el numero a calcular: "))
    print(numero_perfecto(base))
           