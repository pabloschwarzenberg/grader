def jerigonzo(string):
  st=string
  v='aeiouAEIOU'
  a=''
  for i in range(len(st)):
    if st[i] in v:
      a+=st[i]+'p'+st[i]
    else:
      a+=st[i]
  return a
