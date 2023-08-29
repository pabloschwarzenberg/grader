def mcd(a,b):
    if b==0:
        return a
    if a>b:
        r=a%b
        return mcd(b,r)
def mcm(a,b,ab):
    max=mcd(a,b)
    min=(ab)/max
    return min

if __name__=="__main__":
  pass