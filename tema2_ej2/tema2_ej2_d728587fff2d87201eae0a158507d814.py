# completa el código de la función
def amigos(a,b):
    divisores_a=[]
    divisores_b=[]
    for i in range(1,(a-1)):
        if a%i==0:
            divisores_a.append(i)
    for k in range(1,(b-1)):
        if b%k==0:
            divisores_b.append(k)
    if sum(divisores_a)==b:
        return True
    elif sum(divisores_b)==a:
        return True
    else:
        return False

           