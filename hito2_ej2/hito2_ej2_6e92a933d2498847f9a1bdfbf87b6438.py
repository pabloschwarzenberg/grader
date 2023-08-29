string=input()
imp=True
for i in list(string):
  if i.lower() not in ["a", "c", "t", "g"]:
    print("secuencia incorrecta")
    imp=False
if imp:
  print("secuencia correcta")