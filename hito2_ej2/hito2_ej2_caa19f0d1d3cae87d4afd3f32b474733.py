a= str(input("secuencias"))
a= a.upper()
b = len(a)
c = 0
for m in a:
  if m == "A" or m =="C" or m == "T" or m == "G":
    c = c+1
if c == b:
  print("secuencia correcta")
else:
  print("secuencia incorrecta")