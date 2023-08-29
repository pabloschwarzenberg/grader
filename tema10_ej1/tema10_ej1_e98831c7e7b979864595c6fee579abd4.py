def MCD(a,b):
  resto=a%b
  if resto==0:
    return b 
  else:
    return MCD(b,resto)

def mcm(a,b,ab):
    m=ab/MCD(a,b)
    return int(m)

if __name__=="__main__":
    pass
           