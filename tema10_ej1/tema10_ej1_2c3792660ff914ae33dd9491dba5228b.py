def mcm(a,b,ab):
    resto=0
    while(b>0):
        resto=b
        b=a%b
        a=resto
    resultado=(a*b)/a
    return a

 
if __name__=="__main__":
    pass