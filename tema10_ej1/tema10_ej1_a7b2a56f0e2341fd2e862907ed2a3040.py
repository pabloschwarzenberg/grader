def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd
 
def mcm(num1, num2,num3):
    a = max(num1, num2)
    b = min(num1, num2)
    c = (a / mcd(a, b)) * b
    return c

if __name__=="__main__":
    pass
           