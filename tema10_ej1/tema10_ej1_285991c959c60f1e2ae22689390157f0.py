def mcm(a,b,ab):
    resul=ab/(mcd(a,b))
    return int(resul)

def mcd(a,b):
    if a == b:
        print("return final:",a)
        return a
    if a!=b:
        print("a",a,"b",b)
        if a>b:
            a=a-b
            #mcd(a,b)
        if b>a:
            b=b-a
        return mcd(a,b)

if __name__=="__main__":
    pass
           