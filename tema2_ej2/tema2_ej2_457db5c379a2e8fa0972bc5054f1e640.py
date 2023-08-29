# completa el código de la función
def amigos(a,b):
    #se crea lista con los divisores de a
    c=1
    da=[]
    while c<=a:
        if a%c==0:
            da.append(c)
            c+=1
        else:
            c+=1
    # se crea lista con los divisores de b
    v=1
    db=[]
    while v<=b:
        if b%v==0:
            db.append(v)
            v+=1
        else:
            v+=1
    #se suman divisores de a
    sum_da=0
    for i in da:
        sum_da+=i
    #se suman divisores de a
    sum_db=0
    for i in db:
        sum_db+=i
    #Condicion para que sean amigos
    if sum_db==a and sum_da==b:
        return True
    elif sum_db==sum_da:
       return True
    else:
        return False
           