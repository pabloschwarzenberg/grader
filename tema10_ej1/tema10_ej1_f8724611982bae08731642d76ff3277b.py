def mcm(a,b,ab):
    if a>b:
      k=mcd(a,b)
    elif a<b:
      k=mcd(b,a)
    return ab/k

def mcd(a,b):
  #a>b
   c=a%b
   if c==0:
    return int(b)
   else:
     return int(mcd_2(b,c))
def mcd_2(b,c):
   d=b%c
   if d==0:
     return int(c)
   else:
     return mcd_2(c,d)

