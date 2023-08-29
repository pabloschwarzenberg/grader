def mcd(a, b):
  c = a - b
  if c == 0:
    return b
  elif c < 0:
    c += b
    return mcd(b, c)
  else:
    return mcd(c, b)

def mcm(a, b, ab):
  result = ab / mcd(a, b)
  return result

if __name__=="__main__":
  pass
           