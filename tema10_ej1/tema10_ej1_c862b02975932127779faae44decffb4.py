def mcm(a,b,ab):
    def mcd(a,b):
        if a>b:
            if b==0:
                return a

            else:
                a1=b
                b1= a%b
                return mcd(a1,b1)
    mcd=(mcd(a,b))
    mcm=ab/mcd
    return mcm


if __name__=="__main__":
 print(mcm(88,44,88*44))




           