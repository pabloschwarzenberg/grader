def mcm(a,b,ab):
    while b:
      mcd = b
      b = a % b
      a = mcd
    mcm =  (ab) // mcd
    return mcm

if __name__=="__main__":
    num1 = input()
    num2 = input()
    multip = num1*num2
    mcm(num1, num2, multip)
    pass
           