def MCD(a,b):
    if a==b:
        return a
    else:
        if a>b:
            return MCD(a-b,b)
        else:
            return MCD(a,b-a)
def mcm(a,b,ab):
    return int(ab/MCD(a,b))

if __name__=="__main__":
    print(mcm(88,44,88*44))
    
           