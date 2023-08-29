def mcm(a,b,ab):
  if ab == a*b:
    ab=[a,b]
  if a < b:
    x=a
    y=b
  else:
    x=b
    y=a
    ab=ab[::-1]
  if x == y:
    return x
  else:
    return mcm(x+ab[0],y,ab)

if __name__=="__main__":
    pass
           