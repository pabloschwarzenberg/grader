def MCD(a,b):
  if a==b:
    return a
  elif a>b:
    return MCD(a-b,b)
  elif a<b:
    return MCD(a,b-a)

def mcm(a,b,ab):
    mcm = (a*b)/MCD(a,b)
    return mcm

if __name__=="__main__":
    pass
           