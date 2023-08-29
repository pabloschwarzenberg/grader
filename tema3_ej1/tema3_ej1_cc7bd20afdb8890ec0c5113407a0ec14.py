def suma_divisores(n):
    divisor=1
    sumadivisores=0
    b=1
    nd=0
    while divisor<n:
        if n%divisor==0:
            sumadivisores=sumadivisores+divisor
        divisor=divisor+1
    while b<=n:
        if n%b==0:
            nd=nd+1
            b=b+1
        else:
            b=b+1
    if nd>2 or nd==1:
        return(sumadivisores,False)
    else:
        return(sumadivisores,True)