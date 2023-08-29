def suma_divisores(a):
    contador=1
    divisores=0
    sumadivisores=0
    while contador<a:
        posible_divisor= a%contador
        if posible_divisor==0:
            sumadivisores+=contador
            divisores+=1
        contador+=1
    if sumadivisores==1:
        return 1, True  
    elif sumadivisores!=1:
        return sumadivisores,False