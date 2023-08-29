def euclides(a,b):
  c=a%b
  a=b
  if c==0:
    return a
  return euclides(a,c)
def mcm(a,b,w):
  z=euclides(a,b)
  return w/z

if __name__=="__main__":
    a=int(input())
    b=int(input())
    mcm(a,b,a*b)
           