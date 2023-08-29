def mcm(a,b,ab):
    mcd_resto=a%b
    if mcd_resto == 0:
        mcd = b
        mcm = int(ab/mcd)
        return mcm
    else:
        mcd_entero=a//b
        mcd_resto=a%b
        divisor = b
        ab= a*b
    mcm(divisor,mcd_resto,ab_1)

if __name__=="__main__":
    a=int(input("ingrese a: "))
    b=int(input("ingrese b: "))
    ab = a*b
    print(mcm(a,b,ab))