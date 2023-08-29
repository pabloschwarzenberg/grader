def mcd(a,b):
    if a>b:
        NUM=a
        num=b
    else:
        NUM=b
        num=a

    if NUM%num==0:
        return num
    else:
        return mcd(num,NUM%num)
def mcm(a,b,ab):
    return int(ab/mcd(a,b))

if __name__=="__main__":
    pass
           