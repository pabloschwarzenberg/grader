def coprimos(a,b):
    n=min(a,b)
    Flag=True
    for i in range(2,n+1):
        if a%i==0 and b%i==0:
            Flag=False
    return Flag

def mcm(a,b,ab):
    if coprimos(a,b):
        return ab
    elif a%b==0:
        return ab/max(a,b)

    else:
        return int((ab/mcm(b,a%b,(a%b)*b)))
if __name__=="__main__":
    pass
           