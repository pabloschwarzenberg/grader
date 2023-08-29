def mcd(a,b):
    if b==0:
        return a
    else:
        resto=a%b
        min_cd=mcd(b,resto)
        return min_cd

def mcm(a,b,ab):
   if a==b or a==0 or b==0:
        return a
   else:
        MCM=(a*b)/mcd(a,b)
        return MCM

if __name__=="__main__":
    print(88,44,88*44)
    
           