def mcd(a,b):
  if a-(a//b)*b==0:
    return(b)
  a,b=(max(a,b),min(a,b))
  return(mcd(b,a-(a//b)*b))

def mcm(a,b,ab):
    return((ab)/mcd(a,b))
    

if __name__=="__main__":
    pass
           