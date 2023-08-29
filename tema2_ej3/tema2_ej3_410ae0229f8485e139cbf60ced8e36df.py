def numero_perfecto(n):
    a=n-1
    x=0
    if n==1:
        return 0,False
    else:
        while a>=1:
            if n%a==0:
                x+=a
            a-=1
        if x==n:
            return True
        else:
            return False