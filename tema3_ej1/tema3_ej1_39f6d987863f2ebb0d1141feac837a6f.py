def suma_divisores(a):
    suma= 0
    cantidad= 0
    for divisor in range(1,a+1):
        if (a % divisor) == 0 :
            suma += divisor
            cantidad+= 1
    suma= suma - divisor
    cantidad= cantidad - 1
    if suma== 1:
        return (suma,True)
    else: return (suma,False)