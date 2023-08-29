def mcm(a,b,ab):
    if b == 0:
        m = ab / a
        return m
    else:
      c = b
      b = a % b
      a = c
      print(a, b)
      return mcm(a, b , ab)

if __name__=="__main__":
    pass
           