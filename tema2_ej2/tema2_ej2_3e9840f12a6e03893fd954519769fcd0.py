# completa el código de la función


def amigos(a,b):
    divisoresa=[]
    divisoresb=[]
    inicio=1
    inicio2=1
    final=a
    final2=b
    while inicio<final:
        if a%inicio==0:
            divisoresa.append(inicio)
        inicio=inicio+1

    while inicio2<final2:
        if b%inicio2==0:
            divisoresb.append(inicio2)
        inicio2=inicio2+1

    sumaa=sum(divisoresa)
    sumab=sum(divisoresb)

    if sumaa==b and sumab==a:
        return True
        #print("verdadero")
    else:
        return False
        #print("falso")