# completa el código de la función
def amigos(a, b):
    da=list()
    i=1
    while i<a:
        if a%i==0:
            da=da+[i]
        i=i+1
    if sum(da)==b:
        j=1
        db=list()
        while j<b:
            if b%j==0:
                db=db+[j]
            j=j+1
        if sum(db)==a:
            return True
        else:
            return False
    else:
        return False 