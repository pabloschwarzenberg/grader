x=int(input())
if x>999:
    u=x%10
    d=x%100
    d=d//10
    c=x//100
    c=c%10
    m=x//1000
    print(m,"M +", c,"C +",d,"D +",u,"U")
if 99<x<1000:
    u=x%10
    d=x//10
    d=d%10
    c=x//100
    print(c,"C +",d,"D +",u,"U")
if 9<x<100:
    u=x%10
    d=x//10
    print(d,"D +",u,"U")
if 0<=x<10:
    u=x
    print(u,"U")
