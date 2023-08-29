def mcd(a,b):
  if a%b == 0:
    return b
  elif a % b != 0:
    while a % b != 0:
      return mcd(b,a%b)


def mcm(a,b,ab):
    if ab == 0:
      return 0
    elif ab == 1 or ab ==1:
      return 1
    else:
      return ab/mcd(a,b)
            
      
      
    pass

if __name__=="__main__":
    pass
           