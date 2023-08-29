# completa el código de la función
def suma_divisores(a):
    div1 = []
    for divisor1 in range(1,a):
        if (a % divisor1) == 0 :
            div1.append(divisor1)
    if sum(div1) == 1:
        return sum(div1), True
    else:
        return sum(div1), False  
           