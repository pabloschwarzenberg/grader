def mcm(a,b,a*b):
  if a==1 or b==1:
    return a*b
  else:
    i=1
    if a%i==0 and b%i==0:
      a=a/i
      b=b/i
    else:
      i=i+1
      mcm(a,b,a*b)
if __name__=="__main__":
    pass
           