def numero_perfecto(a):
    divisor = []
  
    for i in range(1, a):
        if a % i == 0:
            divisor.append(i)
    if sum(divisor) == a:
        return True
    else:
        return False

    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))