def mcm(a,b,ab):
    if a%b==0:
        return a*b
    else:
        return (mcm(b,a%b,a))

if __name__=="__main__":
    pass
           