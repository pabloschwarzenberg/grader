def mcm(a,b,ab):
    x=max([a,b])
    if b==1:
      x=1
    if a%x==0 and b%x==0:
      return ab/x
    else:
      return mcm(a,b-1,ab)
    pass

if __name__=="__main__":
    pass