def amigos(a,b):
    if a>0 and b>0:
        i=1
        div=0
        seguir=True
        while seguir:
            while i<=(a):
                p=a%i
                if p==0:
                    div=div+i
                div=div
                i=i+1
            m=(div-a)
            g=1
            div1=0
            while g<=(b):
                q=b%g
                if q==0:
                    div1=div1+g
                div1=div1
                g=g+1
            n=(div1-b)
            seguir= False
        if m==b and n==a:
            return True
        else:
            return False
           