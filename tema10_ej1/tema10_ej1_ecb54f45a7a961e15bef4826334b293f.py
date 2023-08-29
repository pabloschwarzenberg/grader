def MCD(y, x):
    if x >= 0 and y >= 0:
        if min(x,y) == 0:
            return max(x,y)
        else:
            return MCD(min(x,y),max(x,y)%min(x,y))

def mcm(x,y,xy):
    if xy % y == 0 and xy % x == 0:
        return int(xy/MCD(y,x))
    return mcm(y,x,(xy)/MCD(y,x))

    

if __name__=="__main__":
    pass
           