def amigos(a,b):
  aa = []
  bb = []
  i = 1
  h = 1
  if a == 1 and b == 1:
    return True
  if a == 1 or b == 1:
    return False
  while sum(aa) < b: 
    if a % i == 0 :
      aa.append(i)
    i = i + 1
  while sum(bb) < a :
    if b % h == 0 :
      bb.append(h)
    h = h + 1 
  if sum(aa) == b and sum(bb) == a:
    return True
  else: 
    return False