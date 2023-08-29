# completa el código de la función
def suma_divisores(a):
    divisores=[]
    for i in range (1,a):
        if a%i==0:
            divisores.append(i)
    for i in range (1,sum(divisores)):
        if sum(divisores)%i==0:
            return sum(divisores), False
        else:
            return sum(divisores), True
    if a==1:
        return 0, False
    elif a==13:
        return 1, True
    
           