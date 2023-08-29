def mcm(a,b,ab):
    if a%b==0:
        return (ab)/b
    else:
        c=a%b
        return mcm(b,c,ab)

if __name__=="__main__":
    pass
           