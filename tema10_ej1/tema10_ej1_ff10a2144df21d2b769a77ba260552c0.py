import math
def mcd(num1,num2):
    a=max(num1,num2)
    b=min(num1,num2)
    while b!=0:
        mcd=b
        b=a%b
        a=mcd
    return mcd

def mcm(a,b,ab):
    mcm=ab/mcd(a,b)
    return mcm

if __name__=="__main__":
    a=int()
    b=int()
    ab=int()
    mcm(a,b,ab)
           