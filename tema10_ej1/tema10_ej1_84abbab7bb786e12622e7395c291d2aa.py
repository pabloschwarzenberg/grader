def mcd(b,r):
  resto=b%r
  if resto==0:
    return b
  else:
    mcd(r,resto)
def mcm(a,b,ab):
    if a>b:
      r=a%b
      return (ab)/mcd(b,r)
    elif a<b:
      r=b%a
      return (ab)/mcd(a,r)
    elif a==b:
      return a


if __name__=="__main__":
    pass
           