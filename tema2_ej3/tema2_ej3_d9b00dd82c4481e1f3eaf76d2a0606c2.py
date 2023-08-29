def numero_perfecto(p):
    sum = 0
    divisor = p
    while divisor > 1:
        divisor = divisor - 1
        if (p % divisor) == 0:
            sum += divisor
    if sum==p:
        return True
    if sum !=p:
        return False
if "_name_"=="_main_":
    a=int(input("Ingrese p: "))
    print(numero_perfecto(p))
           