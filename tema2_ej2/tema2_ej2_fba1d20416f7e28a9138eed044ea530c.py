# completa el código de la función
def amigos(a,b):
    x=1
    td1=0
    td2=0
    while a>=x:
        if (a%x)==0:
            td1+=x
        x+=1
    x=1
    td1=td1-a
    while b>=x:
        if (b%x)==0:
            td2+=x
        x+=1
    td2=td2-b
    if td1==b and td2==a:
        return True
    else:
        return False