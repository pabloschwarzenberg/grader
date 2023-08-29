def mcm(a,b,ab):
    return (ab/mcd(a,b))
   
    pass
def mcd(a,b):
    if a%b==0:
        return b
    else:
        c=a//b
        d=a-(b*c)
        return mcd(b,d)
    pass
if __name__=="__main__":
    print (mcm(a,b,ab))
    pass
           