# completa el código de la función
def amigos(a,b):
    da=[]
    db=[]
    for i in range(1,a):
        if a%i==0:
            da.append(i)
    sumaa=sum(da)

    for j in range(1,b):
        if b%j==0:
            db.append(j)
    sumab=sum(db)

    if sumaa==b and sumab==a :
        return True 
    else :
        return False
           