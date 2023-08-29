def mcm(a,b,ab):
    def MCD(a,b):
        if a>b and a%b==0:
            return float(b)
        elif a>b:
            return MCD(a,a%b)
        elif b>a and b%a==0:
            return float(a)
        elif b>a:
            return MCD(b,b%a)
    return (float(a)*float(b))/MCD(a,b)

print(mcm(88,44,30))
