def numero_perfecto(a):
    divisores=[1]
    for divisor in range(1,a):
        if a%divisor==0:
            divisores.append(divisor)

    resultado=sum(divisores)
    resultado_final=resultado-1
    if resultado_final==a:
        return True

    else:
        return False
           