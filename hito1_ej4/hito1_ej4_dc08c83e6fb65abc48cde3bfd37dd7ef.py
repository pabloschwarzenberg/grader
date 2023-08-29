num=int(input())
num=str(num)
digito=len(num)
num=int(num)
if digito==1:
    a=num%2
    b=(num//2)%2
    c=(num//4)%2
    d=(num//8)
    if d!=0:
        print("resultado=",(d*10**3)+(c*10**2)+(b*10)+a)
    elif d==0:
        if c!=0:
            print("resultado=",(c*10**2)+(b*10)+a)
        elif c==0:
            if b!=0:
                print("resultado=",(b*10)+a)
            elif b==0:
                print("resultado=",a)
if digito==2:
    a=num%2
    b=(num//2)%2
    c=(num//4)%2
    d=(num//8)%2
    e=(num//16)%2
    f=(num//32)%2
    g=(num//64)%2
    if g!=0:
        print("resultado=",(g*10**6)+(f*10**5)+(e*10**4)+(d*10**3)+(c*10**2)+(b*10)+a)
    elif g==0:
        if f!=0:
            print("resultado=",(f*10**5)+(e*10**4)+(d*10**3)+(c*10**2)+(b*10)+a)
        elif f==0:
            if e!=0:
                print("resultado=",(e*10**4)+(d*10**3)+(c*10**2)+(b*10)+a)
            elif e==0:
                print("resultado=",(d*10**3)+(c*10**2)+(b*10)+a)
if digito==3:
    a=num%2
    b=(num//2)%2
    c=(num//4)%2
    d=(num//8)%2
    e=(num//16)%2
    f=(num//32)%2
    g=(num//64)%2
    h=(num//128)%2
    i=(num//256)%2
    j=(num//512)%2
    if j!=0:
        print("resultado=",(j*10**9)+(i*10**8)+(h*10**7)+(g*10**6)+(f*10**5)+(e*10**4)+(d*10**3)+(c*10**2)+(b*10)+a)
    elif j==0:
        if i!=0:
            print("resultado=",(i*10**8)+(h*10**7)+(g*10**6)+(f*10**5)+(e*10**4)+(d*10**3)+(c*10**2)+(b*10)+a)
        elif i==0:
            if h!=0:
                print("resultado=",(h*10**7)+(g*10**6)+(f*10**5)+(e*10**4)+(d*10**3)+(c*10**2)+(b*10)+a)
            elif h==0:
                print("resultado=",(g*10**6)+(f*10**5)+(e*10**4)+(d*10**3)+(c*10**2)+(b*10)+a)
        
        
    


    

              