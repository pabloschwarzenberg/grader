# completa el código de la función
def amigos(a,b):
    da = []
    db = []
    r = False
    i = 1
    j = 1
    for i in range(1,a):
        if a%i==0:
            da.append(i)
            i+1
        else:
            i+1
            continue
    for j in range(1,b):
        if b%j==0:
            db.append(j)
            j+1
        else:
            j+1
            continue
    print(da)
    print(db)
    if sum(list(da))==b and sum(list(db))==a:
        r = True
    else:
        r = False
    return r           