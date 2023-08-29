def mcd(a,b):
    cuociente=a//b
    resto=a-b*cuociente
    if resto==0:
        return b
    else:
       return (mcd(b,resto))

def mcm(a,b,ab):
    return ab/mcd(a,b)

if __name__=="__main__":
    pass
           