import math
n=int(input())
a=int(math.log10(n))+1      #N° Dígitos

if a>4:
     print("Hasta 4 dígitos")
else:
    u=int(n%10)
    d=int((n%100-n%10)/10)
    c=int((n%1000-n%100)/100)
    m=int((n%10000-n%1000)/1000)
    if a==1:
        print(u,"U")
    elif a==2:
        print(d,"D+",u,"U")
    elif a==3:
        print(c,"C+",d,"D+",u,"U")
    else:
        print(m,"M+",c,"C+",d,"D+",u,"U")