def mcm(a,b,ab):
  def mcd(a,b):
    if b == 0:
      return a
    else:
      return mcd(b, a%b)
  return (ab)/(mcd(a,b))
    

if __name__=="__main__":
    pass
           