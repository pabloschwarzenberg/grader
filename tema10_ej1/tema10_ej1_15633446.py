def MCD(a,b):
    if a==b:
        return a
    if a>b:
        return MCD(a-b,b)
    if a<b:
        return MCD(a,b-a)
def mcm(a,b,c):
    return c/MCD(a,b)

if __name__=="__main__":
    pass
           