palabra=input()
palabra.lower()
x=0
for i in palabra:
  if i!="a" and i!="c" and i!="t" and i!="g":
    x=1
if x==0:
  print("secuencia correcta")
if x==1:
  print("secuencia incorrecta")