# completa el código de la función
def amigos(a,b):
    Sumaa = 0
    Sumab = 0
    for i in range(1,a):
        if a%i==0:
            Sumaa +=i
    if Sumaa !=b:
        return False
    for z in range(1,b):
        if b%z == 0:
            Sumab += z
    if Sumab != a:
        return False
    return True