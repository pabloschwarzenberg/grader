def mcd(num1,num2):
    if num1 == num2:
        return num1

    if num1 > num2:
        while num1 % num2 != 0:
            num2 = num1 % num2
        return num2
    if num2 > num1:
        while num2 % num1 != 0:
            num1 = num2 % num1
        return num1




def mcm(a,b,ab):
    return ab//mcd(a,b)

if __name__=="__main__":
    pass
           