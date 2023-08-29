    
def mcd(a,b):
    r=a%b
    a=b
    b=r
    if b==0:
        return a
    else:
      mcd(a,b)
def mcm(a,b,ab):
    d=mcd(a,b)
    c=(ab/d)
    return c
if __name__=="__main__":
    print(str(mcm(88,44,88*44)))
    


           