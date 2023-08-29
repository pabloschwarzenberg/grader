# completa el código de la función

def amigos(a,b):
    i=1
    divA=[]
    while i < a:
        if a%i==0:
            divA.append(i)
        i+=1

    i = 1
    divB = []
    while i < b:
        if b % i == 0:
            divB.append(i)
        i += 1
    if sum(divA) == b and sum(divB) == a:
        return True
    else:
        return False
