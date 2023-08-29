#Cálculo del dígito verificador de un rut
q = int(input())
if q < 10000000:
    RUT = str(q)
    n1=int(RUT[-1])
    n2=int(RUT[-2])
    n3=int(RUT[-3])
    n4=int(RUT[-4])
    n5=int(RUT[-5])
    n6=int(RUT[-6])
    n7=int(RUT[-7])
    n1=n1*2
    n2=n2*3
    n3=n3*4
    n4=n4*5
    n5=n5*6
    n6=n6*7
    n7=n7*2
    s=n1+n2+n3+n4+n5+n6+n7
    l=s//11
    d=l*11
    r=s-d
    num=11-r
    if num != 10 and num != 11:
        print("dv=",num)
    if num == 11:
        print("dv=",0)
    else:
        print("dv=k")
if q < 100000000 and q > 9999999:
    RUT = str(q)
    n1=int(RUT[-1])
    n2=int(RUT[-2])
    n3=int(RUT[-3])
    n4=int(RUT[-4])
    n5=int(RUT[-5])
    n6=int(RUT[-6])
    n7=int(RUT[-7])
    n8=int(RUT[-8])
    n1=n1*2
    n2=n2*3
    n3=n3*4
    n4=n4*5
    n5=n5*6
    n6=n6*7
    n7=n7*2
    n8=n8*3
    s=n1+n2+n3+n4+n5+n6+n7+n8
    l=s//11
    d=l*11
    r=s-d
    num=11-r
    if num != 10 and num != 11:
        print("dv=",num)
    if num == 11:
        print("dv=",0)
    else:
        print("dv=k")
