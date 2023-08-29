def mcm(a,b,ab):
    while a!=b:
      a=min(a,b)
      b=max(a,b)-a
    if a==b:
      mcm=ab/a
    return mcm

if __name__=="__main__":
    pass
           