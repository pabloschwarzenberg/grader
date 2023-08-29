a=int(input())
b=int(input())
def mcm(a,b,ab):
    def mcd(a,b):
        if a<b:
            i=a
        else:
            i=b
        while i>0:
            if a%i==0 and b&i==0:
                return i
            else:
                
                i-=1
    return (a*b)/mcd(a,b)
    

if __name__=="__main__":
    print(mcm(a,b,ab))





