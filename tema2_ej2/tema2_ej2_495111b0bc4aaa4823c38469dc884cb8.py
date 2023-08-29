# completa el código de la función
def amigos(a,b):
    div_a = []
    div_b = []
    for x in range(1,a):
        if a % x == 0:
            div_a.append(x)

    for y in range(1,b):
        if b % y == 0:
            div_b.append(y)

    sum_a = sum(div_a)
    sum_b = sum(div_b)

    if sum_a == b and sum_b == a:
        return True
    else:
        return False
           