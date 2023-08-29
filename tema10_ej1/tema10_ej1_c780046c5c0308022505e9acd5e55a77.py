def mcd(a,b):
    resto=a%b
    if resto==0:
        return int(b)
    else:
        mcd(b,resto)
        return 1

def mcm(a,b,ab):
    mcd_s=mcd(a,b)
    mcm_valor= ab//mcd_s
    return mcm_valor

    

if __name__=="__main__":
    pass
           