def amigos(a,b):
    contador_a=[]
    contador_b=[]
    suma=0
    for i in range(1,a-1):
        if a%i==0:
            contador_a.append(i)
    for r in range(1,b-1):
        if b%r==0:
            contador_b.append(r)
    if sum(contador_a)==b and sum(contador_b)==a:
        return True
    else:
        return False  