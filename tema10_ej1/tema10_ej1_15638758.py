def mcm(a,b,a*b):
    def MCD(a,b):
        if a==b:
            return a
        if a>b:
            return MCD(a-b,b)
        if a<b:
            return MCD(a,b-a)
    return(a*b)/MCD(a,b)

 
