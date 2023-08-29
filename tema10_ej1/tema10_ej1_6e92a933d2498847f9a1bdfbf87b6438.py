def mcd(a,b):
  if a<b:
    a,b=b,a
  if b==1 or a==1:
      return 1
  elif a==b:
      return a
  elif a%b==0:
      return b
  else:
    return mcd(b,a%b)

def mcm(a,b,ab):
    return ab/mcd(a,b)
