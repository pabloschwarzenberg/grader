#Cálculo del dígito verificador de un rut
a=int(input())
if a>=10000000:
    q= a//10000000
    w=(a//1000000)%10
    e=(a//100000)%10
    r=(a//10000)%10
    t=(a//1000)%10
    y=(a//100)%10
    u=(a//10)%10
    i=a%10
    S=i*2+u*3+y*4+t*5+r*6+e*7+w*2+q*3
    f=11-(S-((S//11)*11))
    if f==11:
        print("dv=0")
    elif f==10:
        print("dv=K")
    elif f<10:
        print("dv=",f)
if a<=9999999 :
    w=(a//1000000)
    e=(a//100000)%10
    r=(a//10000)%10
    t=(a//1000)%10
    y=(a//100)%10
    u=(a//10)%10
    i=a%10
    S=i*2+u*3+y*4+t*5+r*6+e*7+w*2
    f=11-(S-((S//11)*11))
    if f==11:
        print("dv=0")
    elif f==10:
        print("dv=K")
    elif f<10:
        print("dv=",f)