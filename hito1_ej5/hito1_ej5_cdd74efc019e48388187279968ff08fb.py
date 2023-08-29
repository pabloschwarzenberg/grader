#Cálculo del dígito verificador de un rut
l=input("inserte su rut, sin código verificador")
if int(l)<10000000:
    a=int(l[6])*2
    b=int(l[5])*3
    c=int(l[4])*4
    d=int(l[3])*5
    e=int(l[2])*6
    f=int(l[1])*7
    g=int(l[0])*2
    x=a+b+c+d+e+f+g
    y=x/11
    o=int(y)
    q=11*o
    z=11-(x-q)
    if z==11:
        print("dv=0")
    elif z==10:
        print ("dv=k")
    else:
        print("dv=",z)
elif int(l)>=10000000:
    a=int(l[7])*2
    b=int(l[6])*3
    c=int(l[5])*4
    d=int(l[4])*5
    e=int(l[3])*6
    f=int(l[2])*7
    g=int(l[1])*2
    h=int(l[0])*3
    x=a+b+c+d+e+f+g+h
    y=x/11
    o=int(y)
    q=11*o
    z=11-(x-q)
    if z==11:
        print("dv=0")
    elif z==10:
        print ("dv=k")
    else:
        print("dv=",z)
