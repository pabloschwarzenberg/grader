def amigos(a,b):
    sda=0
    sdb=0
    for i in range(1,a):
        da=a/i
        if da==int(da):
            sda=sda+i
    for i in range(1,b):
        db=b/i
        if db==int(db):
            sdb=sdb+i

    if sda==b and sdb==a:
        print("Amigos")
        return True
    else:
        print("Enemigos")
        return False