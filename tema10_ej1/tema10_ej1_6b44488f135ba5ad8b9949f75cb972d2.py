def mcm(a,b,ab):
    return ab/mcd(a,b)
def mcd(a,b):
  x=a
  y=b
  if x==y:
    return x
  else:
    if x>y:
      x=a-b
    else:
      y=a
      x=b-a
    return mcd(x,y)
    
    
if __name__=="__main__":
    pass
           