def mcm(a, b, ab):        
    if a<=b:
        if (b%a)==0:
            mcd = a
            x = (ab)/mcd
            return x
        else:
            return mcm(a,b%a, ab)
    else:
        if (a%b)==0:
            mcd = b
            x = (ab)/mcd
            return x
        else:
            return mcm(b, a%b, ab)

if __name__=="__main__":
    pass
           