s=input("g:")
l=len(s)
for i in range(l):
  c=s[i]
  if c!="A" or c!="C" or c!="T" or c!="G" or c!="a" or c!="c" or c!="t" or c!="g":
    print("secuencia incorrecta")
  else:
    print("secuencia correcta")