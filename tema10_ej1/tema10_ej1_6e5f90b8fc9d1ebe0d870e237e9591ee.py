def mcm(num1, num2,num3):
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd

    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd) * b

    return mcm

if __name__=="__main__":
    pass
           