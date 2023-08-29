def mcm(a,b,ab):
    def euc(l,f):
        while l!=f:
            if l>f:
                l=l-f
            else:
                f=f-l
        return l
    return a*b/euc(a,b)
   

if __name__=="__main__":
    pass
           