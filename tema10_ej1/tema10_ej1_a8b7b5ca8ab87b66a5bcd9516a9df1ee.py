def MCDRecursivo(a,b):
    if( a < b):
        return MCDRecursivo(b,a)
    elif(b==0):
        return a
    else:
        return MCDRecursivo(b, a%b)

def mcm(a,b,ab):
    mcd=MCDRecursivo(a,b)
    mcm=(ab)/mcd
    return mcm


if __name__=="__main__":
    a=int(input())
    b=int(input())
    ab=int(input())
    

    print(mcm(a,b,ab))


           