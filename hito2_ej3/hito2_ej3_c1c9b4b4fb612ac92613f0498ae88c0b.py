def separado(s,n):
  o=s
  l=[]
  i=0
  while i<n:
    if i>=1:
      if s[:n] in l:
        while s[:n] in l:
          pos=l.index(s[:n])
          l.pop(pos)
      else:
        l.append(s[:n])
        s=s[n:]
    else:
      l.append(s[:n])
      s=s[n:]
    i+=1
  return l
st=(input('ingrese cadena')).upper()
n=int(input('ingrese largo de cadena'))
a=separado(st,n)
if len(a)>0:
  i=0
  while i < len(a):
    print (a)
    i+=1
else:
  print('ninguna')