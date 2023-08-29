def mcm(a,b,ab):

  def mcd(a,b):
    if b==0:
      return a
    c=a%b
    a=b
    return mcd(a,c)
  return ab/mcd(a,b)

if __name__=="__main__":
    pass
           