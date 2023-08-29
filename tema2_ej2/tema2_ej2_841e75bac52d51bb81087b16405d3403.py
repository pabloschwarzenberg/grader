# completa el código de la función
def amigos(a,b):
    divA = []
    divB = []
    for i in range(1, a):
        if a%i == 0:
            divA.append(i)
            
    for i in range(1, b):
        if b%i == 0:
            divB.append(i)

    if sum(divA) == b and sum(divB) == a:
        return True
    
    else:
        return False
           