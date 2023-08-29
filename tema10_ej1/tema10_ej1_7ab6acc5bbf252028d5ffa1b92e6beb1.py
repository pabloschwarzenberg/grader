def mcd(a,b):
    if b==0:
       return a
    r=a%b
    return mcd(b,r)
def mcm(a,b,c):
    return c/mcd(a,b)
    

if __name__=="__main__":
    print(mcm(88,44,88*44))
           