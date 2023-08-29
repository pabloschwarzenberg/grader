def amigos(a,b):
    div1=a-1
    sumdiv=0
    if a==1:
        sumdiv=1
    if a!=1:
        while div1!=0:
            if a%div1==0:
                divisor=div1
                sumdiv=sumdiv+divisor
            div1=div1-1
    div2=b-1
    sumdiv2=0
    if b==1:
        sumdiv2=1
    if b!=1:
        while div2!=0:
            if b%div2==0:
                divisor=div2
                sumdiv2=sumdiv2+divisor
            div2=div2-1
    x=sumdiv
    y=sumdiv2
    print(sumdiv,sumdiv2)
    if x==b and y==a:
        fin=True
    else:
        fin=False
    return fin
