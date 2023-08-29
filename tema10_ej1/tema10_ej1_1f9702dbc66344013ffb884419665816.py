def mcm(a,b,ab):
    if a%b==0:
      mcd=b
      MCM=ab/mcd
      return MCM
    else:
      resto=a%b
      return mcm(b,resto,ab)
if __name__=="__main__":
    pass
           