print("ingrese los valores de: ")
x=int(input("rut= "))
if 9999999<x<100000000:
    x1=x%10
    n1=x//10
    x2=n1%10
    n2=n1//10
    x3=n2%10
    n3=n2//10
    x4=n3%10
    n4=n3//10
    x5=n4%10
    n5=n4//10
    x6=n5%10
    n6=n5//10
    x7=n6%10
    n7=n6//10
    x8=n7%10
    
    y1=x1*2
    y2=x2*3
    y3=x3*4
    y4=x4*5
    y5=x5*6
    y6=x6*7
    y7=x7*2
    y8=x8*3

    z=y1+y2+y3+y4+y5+y6+y7+y8

    r=(z%11)
    p=11-r
    if p==11:
        print("dv=0")
    elif p==10:
        print("dv=k")
    else :
        print("dv= ",p)
elif 999999<x<10000000:
    x1=x%10
    n1=x//10
    x2=n1%10
    n2=n1//10
    x3=n2%10
    n3=n2//10
    x4=n3%10
    n4=n3//10
    x5=n4%10
    n5=n4//10
    x6=n5%10
    n6=n5//10
    x7=n6%10

    y1=x1*2
    y2=x2*3
    y3=x3*4
    y4=x4*5
    y5=x5*6
    y6=x6*7
    y7=x7*2

    z=y1+y2+y3+y4+y5+y6+y7

    r=(z%11)
    p=11-r
    if p==11:
        print("dv=0")
    elif p==10:
        print("dv=k")
    else :
        print("dv=",p)
