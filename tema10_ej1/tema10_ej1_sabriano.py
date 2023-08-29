def mcm(a,b,ab):
  if a%b!=0:
    mcm(b,a%b,ab)
  else:
    mcd=b
  mcm1=(a*b)/mcd
  return mcm1


if __name__=="__main__":
    pass
           