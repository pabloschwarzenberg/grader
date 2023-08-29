# completa el código de la función
def amigos(a,b):
    contador1 = 1
    contador2 = 1
    count1 = 0
    count2 = 0
    for i in range(a-1):
        if (a % contador1) == 0:
            count1 = contador1 + count1
            contador1 += 1
        else:
            contador1 += 1
    for x in range(b-1):
        if (b % contador2) == 0:
            count2 = contador2 + count2
            contador2 += 1
        else:
            contador2 += 1
    if count1 == b and count2 ==a:
        return True
    else:
        return False
