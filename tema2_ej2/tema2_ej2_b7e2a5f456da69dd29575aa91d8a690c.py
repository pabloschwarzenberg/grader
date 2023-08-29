# completa el código de la función
def amigos(a,b):
    suma_div1 = 0
    suma_div2 = 0
    for x in range(1, a):
        if a % x == 0:
            suma_div1+=x
    for y in range(1, b):
        if b % y == 0:
            suma_div2+=y
    if suma_div1 == b and suma_div2 == a:
        return True
    else:
        return False
           