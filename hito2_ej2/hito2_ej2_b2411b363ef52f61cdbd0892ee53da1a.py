a=input()
l=list(a)
if l.count("A") + l.count("C") + l.count("T") + l.count("G")==len(l):
  print("secuencia correcta")
else:
  print("secuencia incorrecta")