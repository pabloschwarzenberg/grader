b=str(input())
b=b.lower()
b_l=list(b)
for n in b_l:
  if n!="a" or n!="c" or n!="t" or n!="g":
      print("secuencia incorrecta")
  else:
      print("secuencia correcta")
  