def mcm(a,b,ab):
    mcm=ab/mcd(a,b)
    return mcm
def mcd(a,b):
  Resto=a%b
  if Resto==0:
    return b
  else:
    return mcd(b,Resto)
if __name__=="__main__":
    pass
           