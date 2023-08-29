def buscarTodas(a,b):
  a = str(a)
  b = str(b)
  d= ""
  e = ""
  if b in a:
    d = []
    d.append(a.find(b))
    d1 = int(d[-1])
    while d1 != len(a) - 1:
      palabra_temporal = a[d1 + 1:]
      if b not in palabra_temporal:
        break
      else:
        if b in palabra_temporal:
          d.append(palabra_temporal.find(b) + d1 + 1)
          d1 = int(d[-1])
    for item in d:
      e += str(item)
      if item == d[-1]:
        break
      e += " "
  return e
           