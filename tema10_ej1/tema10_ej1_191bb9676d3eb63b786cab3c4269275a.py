def mcm(a,b,ab):
  l = [a,b]
  if max(l) % min(l) == 0:
    return max(l)
  else:
    return ab
