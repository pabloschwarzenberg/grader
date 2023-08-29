# completa el código de la función
def amigos(a, b):
    #Suma Divisores A
    listaA = []
    numeroa = a - 1
    while numeroa > 0:
        if a % numeroa == 0:
            listaA.append(numeroa)
        numeroa -= 1
    sumaa=0
    for item_a in listaA:
        sumaa = sumaa + item_a
    # Fin Suma Divisores A

    # Suma Divisores B
    listaB = []
    numerob = b - 1
    while numerob > 0:
        if b % numerob == 0:
            listaB.append(numerob)
        numerob -= 1
    sumab = 0
    for item_b in listaB:
        sumab = sumab + item_b
    # Fin Suma Divisores B
    if sumaa == b and sumab == a:
        return True
    else:
        return False
           