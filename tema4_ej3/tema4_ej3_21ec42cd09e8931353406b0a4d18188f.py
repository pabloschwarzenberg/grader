def jerigonzo(string):
  st=string
  vo='aeiouAEIOU'
  r=''
  for i in range(len(st)):
    if st[i] in vo:
      r+=st[i]+'p'+st[i]
    else:
      r+=st[i]
  return r