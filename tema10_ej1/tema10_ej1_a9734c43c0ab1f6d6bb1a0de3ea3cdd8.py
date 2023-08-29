def mcm(a,b,ab):
    if b == 0:
        return int((ab)/a)
    else:
        return mcm(b,a%b,ab)
    
if __name__=="__main__":
    a = int(input())
    b = int(input())
    ab = a*b
    print(mcm(a,b,ab))

           