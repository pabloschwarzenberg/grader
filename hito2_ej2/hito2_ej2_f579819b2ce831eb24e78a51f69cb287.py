a=input()
a=list(a)
b=True
for i in range(0,len(a)):
  if a[i] in ["A","C","T","G"]:
    continue
  else:
    global b
    b=False
    print("Secuencia incorrecta")
    break
if b==True:
  print("Secuencia correcta")