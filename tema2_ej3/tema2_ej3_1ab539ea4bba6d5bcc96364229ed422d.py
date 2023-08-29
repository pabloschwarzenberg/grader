def numero_perfecto(a):
    t=1
    r=0
    while t<a:
        if a%t==0:
            r=r+t
            t=t+1
        else:
            r=r
            t=t+1
    if r==a:
        return True
    else:
        return False
 
           