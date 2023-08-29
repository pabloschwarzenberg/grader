def mcd(a,d):
    if(d==0):
     return a
    else:
        return mcd(d,a%d)
def mcm(a,b,ab):
    return int(ab/mcd(a,b))

if __name__=="__main__":
    pass
           