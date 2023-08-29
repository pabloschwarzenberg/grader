def blabla(s):
  k=s.lower()
  a=k.count("t")
  b=k.count("a")
  c=k.count("g")
  d=k.count("c")
  suma=a+b+c+d
  return suma
s=str(input())
if blabla(s)==len(s):
  print("La secuencia {0} es correcta".format(s))
else:
  print("La secuencia {0} es incorrecta".format(s))