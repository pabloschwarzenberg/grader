#Números Amigos
def amigos(a,b):
    divisoresa=[]
    for i in range(1,a):
        if a%i==0:
            divisoresa.append(i)
    suma1=0
    for j in divisoresa:
        suma1= suma1+j
    divisoresb=[]
    for k in range(1,b):
        if b%k==0:
            divisoresb.append(k)
    suma2=0
    for l in divisoresb:
        suma2= suma2+l
    if suma1==b and suma2==a:
        return True
    else:
        return False