a=input()
c=0
for i in range(0,len(a)):
 if a[i]!="a" or a[i]!="c" or a[i]!="t" or a[i]!="g":
  print("secuencia incorrecta")
  c=c+1
if c==0:
 print("secuencia correcta")
 