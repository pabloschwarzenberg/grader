def jerigonzo(s):
    n=list(s)
    l=len(n)
    for i in range(l):
        f=n[i]
        if  f=="a" or f=="e" or f=="i" or f=="o" or f=="u" :
            n[i]=f+"p"+f
    return (''.join(n))
         