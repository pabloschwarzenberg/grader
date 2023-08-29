# completa el código de la función
def amigos(a,b):
    div_a=[]
    div_b=[]
    for i in range(1,a):
        if a % i ==0:
            div_a.append(i)

    for i in range(1,b):
        if b%i==0:
            div_b.append(i)

    sum_a=sum(div_a)
    sum_b=sum(div_b)
    if sum_a ==b and sum_b==a:
       return True
    else:return False