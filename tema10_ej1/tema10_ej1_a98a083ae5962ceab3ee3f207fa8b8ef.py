def mcd(a,b):
    if b==0:
        return a
    else:
        return mcd(b,(a%b))

def mcm(a,b,ab):
    resultado=ab/(mcd(a,b))
    return resultado

if __name__=="__main__":
    pass
           