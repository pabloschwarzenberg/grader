def mcd(a,b):
  if a>b:
    a = a
    b = b
  else:
    a = b
    b = a
  division = divmod(a,b)
  while division[1]!=0:
    a = b
    b = division[1]
    division = divmod(a,b)
    return b
def mcm(a,b,ab):
  c=mcd(a,b)
  mcm=((ab)/c)
  return mcm
if __name__=="__main__":
    pass
           