def mcm(a,b,ab):
    return a*b/mcd(a,b)

def mcd(a,b):
    
    if a<0 or b<0: 
        return ("Error. No se puede encontrar un MCD!")
    elif a==b:
        return a
    else:
        if a>b:
            a=a-b
        else:
            b=b-a
        return mcd(a,b)
        

if __name__=="__main__":
    
    print (mcm(88,44,88*44))
