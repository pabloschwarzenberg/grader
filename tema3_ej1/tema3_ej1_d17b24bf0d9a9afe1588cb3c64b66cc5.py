# completa el código de la función
def suma_divisores(a):
    if a == 1:
        return (0,False)
    elif a == 2:
        return (1, True)
    else:
        divisor = [1]
        for i in range(2, a):
            if a % i == 0:
                divisor.append(i)
        if sum(divisor)== 1:
            return sum(divisor), True
        else:
            return sum(divisor), False