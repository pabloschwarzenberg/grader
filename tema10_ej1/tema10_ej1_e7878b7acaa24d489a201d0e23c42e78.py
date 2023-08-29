def mcm(a,b,ab):
    return ab//mcd(a,b)
def mcd(a,b):
    print("hola")
    if b == 0:
        return a
    else:
        resto=a%b
        return mcd(b,resto)

if __name__=="__main__":
    pass
           