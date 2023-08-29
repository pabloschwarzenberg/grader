def mcd(a,b):
    if a>b:
      if b!=0:
          q=a//b
          r=a%b
          return mcd(b,r)
      else:
          return a
    elif a<b:
      if a!=0:
          q=b//a
          r=a%b
          return mcd(a,r)
      else:
          return b
def mcm(a,b,ab):
    if a>b:
         return (ab)//mcd(a,b)
    else:
         return (ab)//mcd(b,a)
        
      

if __name__=="__main__":
    pass
           