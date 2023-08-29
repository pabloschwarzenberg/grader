def mcd(a,b):
  if a<b:
    return mcd(b,a)
  elif b==0:
    return a
  else:
    return mcd(b,a%b)
    

def mcm(a,b,ab):
    return (a*b)/mcd(a,b)

if __name__=="__main__":
    pass
           