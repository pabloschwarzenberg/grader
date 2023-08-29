def mcm(a,b,ab):
    R = int(ab/mcd(a,b))
    return R
def mcd(a,b):
    if b == 0:
       return a 
    else:
       return mcd(b, a % b)

if __name__=="__main__":
    print(mcm(88,44,88*44))