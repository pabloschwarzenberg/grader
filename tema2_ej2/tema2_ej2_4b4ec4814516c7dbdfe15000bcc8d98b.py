# completa el código de la función
def amigos(a,b):
    
    div_a=[]
    for i in range(1,a):
        if a%i==0:
            div_a.append(i)
    suma_a=sum(div_a)
            
    div_b=[]
    for i in range(1,b):
        if b%i==0:
            div_b.append(i)
    suma_b=sum(div_b)

    if suma_a==b and suma_b==a:
        return True
    else:
        return False