a=input()
b=0
for i in range(len(a)):
  if (a[i] == "A") or (a[i] == "G") or (a[i] == "C") or (a[i] == "T"):
    b += 1
  else:  
    b+=0
if b==len(a):
  print("secuencia correcta")
else:
  print("secuencia incorrecta")