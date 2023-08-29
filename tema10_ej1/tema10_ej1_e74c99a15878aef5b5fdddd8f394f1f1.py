def mcm(a,b,ab):
    i=2
    while i<=a and i<=b:
        if a%i==0 and b%i==0:
            return mcm(a/i,b,ab/i)
        i+=1
    return ab

if __name__=="__main__":
    pass
           