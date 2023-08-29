def mcm(a,b,ab):
    c=max(a,b)%min(a,b)
    if c==0:
      return ab/min(a,b)
    return mcm(min(a,b),c,ab)
    


if __name__=="__main__":

    pass
           