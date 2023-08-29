def rev_cadenas(s):
  s=s.upper()
  s_l= list(s)
  for m in s_l:
    if (m=='A')or(m=='C')or(m=='G')or(m=='T') :
      s_l.remove(m)
  if len(s_l)==0:
    return('secuencia correcta')
  else:
    return('secuencia incorrecta') 
s=input()
print(rev_cadenas(s))