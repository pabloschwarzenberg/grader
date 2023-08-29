r=int(input("rut"))
if r<10000000 :
    m=int(r%10)
    n=int((r%100)/10)
    v=int((r%1000)/100)
    b=int((r%10000)/1000)
    o=int((r%100000)/10000)
    p=int((r%1000000)/100000)
    l=int((r%10000000)/1000000)
    mv=m*2
    nv=n*3
    vv=v*4
    bv=b*5
    ov=o*6
    pv=p*7
    lv=l*2
    sum1=int((mv+nv+vv+bv+ov+pv+lv)/11)
    rest1=(mv+nv+vv+bv+ov+pv+lv)-(11*sum1)
    det1=11-rest1
    if det1==11 :
        print("dv=0")
    elif det1==10 :
        print("dv=k")
    else :
        print("dv=",det1)
else:
    q=int(r%10)
    c=int((r%100)/10)
    u=int((r%1000)/100)
    t=int((r%10000)/1000)
    r=int((r%100000)/10000)
    e=int((r%1000000)/100000)
    w=int((r%10000000)/1000000)
    x=int((r%100000000)/10000000)
    qv=q*2
    cv=c*3
    uv=u*4
    tv=t*5
    rv=r*6
    ev=e*7
    wv=w*2
    xv=x*3
    sum2=int((qv+cv+uv+tv+rv+ev+wv+xv)/11)
    rest2=(qv+cv+uv+tv+rv+ev+wv+xv)-(11*sum2)
    det2=11-rest2
    if det2==11 :
        print("dv=0")
    elif det2==10 :
        print("dv=k")
    else :
        print("dv=",det2)
