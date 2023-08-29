def mcd(a,b):
    mini=min(a,b)
    maxi=max(a,b)
    if mini==0:
        return maxi
    else:
        q=maxi//mini
        r=maxi%mini
        return mcd(mini,r)

def mcm(a,b,ab):
    return int(ab/mcd(a,b))

if __name__=="__main__":
    a=int(input("N° 1: "))
    b=int(input("N° 2: "))
    print(mcm(a,b,a*b))
           