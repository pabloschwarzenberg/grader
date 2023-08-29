def mcm(a,b,ab):
  def mcd(a,b):
    if a == b:
        return a
    elif a > b:
        return mcd(a-b, b)
    elif a < b:
        return mcd(a, b-a)
  return (a*b)/mcd(a,b)
if __name__=="__main__":
    pass
           