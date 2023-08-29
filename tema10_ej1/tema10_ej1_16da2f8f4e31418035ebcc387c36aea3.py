def mcm(a,b,ab):
    if b==0:
        return ab/a
    if a>b:
        r=a%b
        return mcm(b,r,ab)
    else:
        r=b%a
        return mcm(a,r,ab)

if __name__=="__main__":
    print(mcm(input(),input(),input()))
           