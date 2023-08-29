def mcm(a,b,ab):
    if a%b==0:
        return int(ab/b)
    return mcm(b,a%b,ab)
    pass

if __name__=="__main__":
    a=int(input())
    b=int(input())
    ab=a*b
    mcm(a,b,ab)
    pass
           