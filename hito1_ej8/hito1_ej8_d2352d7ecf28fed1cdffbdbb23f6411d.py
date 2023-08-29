n=input()

if len(n)==1:
    print(n,"U")

elif len(n)==2:
    d=n[0:1]
    u=n[1:2]
    print(d,"D +",u,"U")

elif len(n) == 3:
    c=n[0:1]
    d=n[1:2]
    u=n[2:3]
    print( c, "C +", d, "D +", u, "U")

elif len(n) == 4:
    m=n[0:1]
    c=n[1:2]
    d=n[2:3]
    u=n[3:4]
    print(m,"M +",c,"C +",d,"D +",u,"U")