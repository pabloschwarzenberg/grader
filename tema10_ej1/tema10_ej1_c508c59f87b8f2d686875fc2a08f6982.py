def mcm(a,b,ab):
    if a>b:
        resto=a%b
        divisor=b
        if resto==0:
            m=ab/b
            return m
        else:
            mcm(divisor,resto,divisor*resto)
    if b>a:
        resto=b%a
        divisor=a
        if resto==0:
            m=ab/b
            return m
        else:
            mcm(divisor,resto,divisor*resto)

if __name__=="__main__":
    pass
           