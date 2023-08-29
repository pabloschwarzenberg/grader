a= input()
b=0 
for i in range(len(a)):
  if (a[i] == "A") or (a[i] == "G") or (a[i] == "C" or a[i] == "T"):
    b = b + 1
  else:
     b=b
if b == len(a):
  print("secuencia correcta")
else:
   print("secuencia incorrecta")