def mcm(a,b,ab):
    micomu=0
    if (a//2!=0 and b//2==0) or a//2==0 and b//2!=0:
        return ab
    if a//2==0 and b//2==0:
        if a<b:
            expre=b/a
            expres=int(expre//2)
            if expres==0:
                micomu=expres
                return micomu
            else:
                expre=a/expres
                return mcm(a,expres,a*expres)
        if b<a:
            expre=a/b
            expres=int(expre//2)
            if expres==0:
                micomu=expres
                return micomu
            else:
                expre=b/expres
                return mcm(expres,b,expres*b)        

if __name__=="__main__":
    print(mcm(44,88,88*44))
           