def mcd(a,b):
    if a>b:
        resto=a%b
        if resto==0:
            return b
        else:
            resto=mcd(b,resto)
            return resto
    if b>a:
        resto=b%a
        if resto==0:
            return a
        else:
            resto=mcd(a,resto)
            return resto
def mcm(a,b,c=0):
    m=a*b/mcd(a,b)
    return m
        
            
        

if __name__=="__main__":
    print(mcm(72,16))
    print(mcm(54,90))
    print(mcm(88,44))
           