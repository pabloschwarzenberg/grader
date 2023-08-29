a=int(input())

if a<10:
    u=str(a)
    print(u+"U")

elif 9<a<100:
    a=str(a)
    d=(a[0])
    u=(a[1])        
    print(d+"D +",u+"U")

elif 99<a<1000:
    a=str(a)
    c=(a[0])
    d=(a[1])
    u=(a[2])
    print(c+"C +",d+"D +",u+"U")

elif 999<a<10000:
    a=str(a)
    m=(a[0])
    c=(a[1])
    d=(a[2])
    u=(a[3])
    print(m+"M +",c+"C +",d+"D +",u+"U")
