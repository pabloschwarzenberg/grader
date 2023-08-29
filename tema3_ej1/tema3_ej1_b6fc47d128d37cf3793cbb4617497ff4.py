def suma_divisores(a):
    z=0
 
    b=1
    sumatoria=0
    while b<a:
         c=a/b
         if c%1==0:
             if b<a:
               sumatoria+=b
         b=b+1
    if sumatoria==1:
        return sumatoria, True
    else:
        return sumatoria, False

