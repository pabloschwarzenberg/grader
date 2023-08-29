n=input()

if len(n)==7:
    n1=int(n[0:1])*2
    n2=int(n[1:2])*7
    n3=int(n[2:3])*6
    n4=int(n[3:4])*5
    n5=int(n[4:5])*4
    n6=int(n[5:6])*3
    n7=int(n[6:7])*2

    s=n1+n2+n3+n4+n5+n6+n7

    a=s%11

    if a==0:
        print("dv=0")

    else:
        dv=11-a
        if dv==10:
            print("dv=k")
        else:
            print("dv=",dv)

elif len(n)==8:
    n1=int(n[0:1])*3
    n2=int(n[1:2])*2
    n3=int(n[2:3])*7
    n4=int(n[3:4])*6
    n5=int(n[4:5])*5
    n6=int(n[5:6])*4
    n7=int(n[6:7])*3
    n8=int(n[7:8])*2
    s=n1+n2+n3+n4+n5+n6+n7+n8

    a=s%11
    if a==0:
        print("dv=0")
    else:
        dv=11-a
    
        if dv==10:
            print("dv=k")
        else:
            print("dv=",dv)