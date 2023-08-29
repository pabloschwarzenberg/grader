def mcd(a,b):
  if b==0:
    return a
  else:
    return mcd(b,a%b)
def mcm(a,b,ab):
    return (ab/mcd(a,b))

    pass

if __name__=="__main__":
    pass
           