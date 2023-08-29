# completa el código de la función
def amigos(a,b):
    div1 = []
    for divisor1 in range(1,a):
        if (a % divisor1) == 0 :
            div1.append(divisor1)
    div2 = []
    for divisor2 in range(1,b):
        if (b % divisor2) == 0 :
            div2.append(divisor2)
    if sum(div1) == b and sum(div2) == a:
        amigos = True
    else:
        amigos = False
    return amigos

