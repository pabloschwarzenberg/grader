def amigos(a,b):
    c=1
    cant=0
    while c<=a//2:
        if a%c==0:
            cant+=c
        c+=1
    if cant==b:
        c=1
        cant=0
        while c<=b//2:
            if b%c==0:
                cant+=c
            c+=1
        if cant==a:
            return True
        else:
            return False
    else:
        return False