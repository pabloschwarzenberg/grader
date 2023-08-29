def mcm(a,b,ab):
  def mcd(a,b):    
    if b!=0:
      c=b
      b=a%b
    if b==0:
      return c
    if b!=0:
      return mcd(a,b)
  return (a*b)/mcd(a,b)                        