#Descomponer un número
a=str(input())
if len(a)==1:
    print(a,"U")
elif len(a)==2:
    u = a[1:2]
    d = a[0:1]
    print(d, "D +", u, "U")
elif len(a)==3:
    u = a[2:3]
    d = a[1:2]
    c = a[0:1]
    print(c, "C +", d, "D +", u, "U")
elif len(a)==4:
    u=a[3:4]
    d=a[2:3]
    c=a[1:2]
    m=a[0:1]
    print(m,"M +",c,"C +",d,"D +",u,"U")
