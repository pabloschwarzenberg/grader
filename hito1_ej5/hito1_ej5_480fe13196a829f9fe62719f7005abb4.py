r=input("numero de rut")
if len(r)==8:
    a=(int(r[7:])*2)
    b=(int(r[6:7])*3)
    c=(int(r[5:6])*4)
    d=(int(r[4:5])*5)
    e=(int(r[3:4])*6)
    f=(int(r[2:3])*7)
    g=(int(r[1:2])*2)
    h=(int(r[:1])*3)
    s1=(a+b+c+d+e+f+g+h)
    p1=s1//11
    k1=s1-(11*p1)
    m1=11-k1
    if m1==11:
        print ("dv=0")
    elif m1==10:
        print ("dv=K")
    else:
        print ("dv=",m)

elif len(r)==7:
    b2=(int(r[6:])*2)
    c2=(int(r[5:6])*3)
    d2=(int(r[4:5])*4)
    e2=(int(r[3:4])*5)
    f2=(int(r[2:3])*6)
    g2=(int(r[1:2])*7)
    h2=(int(r[:1])*2)
    s=(b2+c2+d2+e2+f2+g2+h2)
    p=s//11
    k=s-(11*p)
    m=11-k
    if m==11:
        print ("dv=0")
    elif m==10:
        print ("dv=K")
    else:
        print ("dv=",m)
