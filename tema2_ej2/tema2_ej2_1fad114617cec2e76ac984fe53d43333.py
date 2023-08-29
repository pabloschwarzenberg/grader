def amigos(a,b):
    divisor1=a-1
    divisor2=b-1
    sumadivisores1=0
    sumadivisores2=0
    while divisor1>1:
        if a%divisor1==0:
            sumadivisores1=sumadivisores1+divisor1
            divisor1=divisor1-1
        elif a%divisor1!=0:
            divisor1=divisor1-1
    t=sumadivisores1
    while divisor2>1:
        if b%divisor2==0:
            sumadivisores2=sumadivisores2+divisor2
            divisor2=divisor2-1
        elif a%divisor2!=0:
            divisor2=divisor2-1
    l=sumadivisores2
    if t==b and l==a:
        return True
    else:
        return False
           