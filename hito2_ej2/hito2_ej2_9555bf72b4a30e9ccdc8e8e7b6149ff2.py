cadena=input().lower()
l=1
for i in cadena:
  if i not in "actg":
    print("secuencia incorrecta")
    i=0
if l==1:
  print("secuencia correcta")