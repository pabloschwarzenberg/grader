#Cálculo del dígito verificador de un rut
x=int(input())
if 9999999<x<100000000:
    a=x//10000000
    b=(x//1000000)%10
    c=(x//100000)%10
    d=(x//10000)%10
    e=(x//1000)%10
    f=(x//100)%10
    g=(x//10)%10
    h=x%10
    a1=a*3
    b1=b*2
    c1=c*7
    d1=d*6
    e1=e*5
    f1=f*4
    g1=g*3
    h1=h*2
    suma=a1+b1+c1+d1+e1+f1+g1+h1
    resto=suma%11
    dig=11-resto
    if dig==10:
        print("dv=k")
    else:
        print("dv=",dig)
if 999999<x<10000000:
    a=x//1000000
    b=(x//100000)%10
    c=(x//10000)%10
    d=(x//1000)%10
    e=(x//100)%10
    f=(x//10)%10
    g=x%10
    a1=a*2
    b1=b*7
    c1=c*6
    d1=d*5
    e1=e*4
    f1=f*3
    g1=g*2
    suma=a1+b1+c1+d1+e1+f1+g1
    resto=suma%11
    dig=11-resto
    if dig==11:
        print("dv=0")
    if dig==10:
        print("dv=k")
    else:
        print("dv=",dig)      