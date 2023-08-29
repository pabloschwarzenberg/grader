n=int(input())
if n>=1000 :
    m=int(n/1000)
    c=int((n%1000)/100)
    d=int((n%100)/10)
    u=int(n%10)
    print(m,"M+",c,"C+",d,"D+",u,"U")
elif n>=100 :
    c=int((n%1000)/100)
    d=int((n%100)/10)
    u=int(n%10)
    print(c,"C+",d,"D+",u,"U")
elif n>=10 :
    d=int((n%100)/10)
    u=int(n%10)
    print(d,"D+",u,"U")
elif n>=0 :
    u=int(n%10)
    print(u,"U")

