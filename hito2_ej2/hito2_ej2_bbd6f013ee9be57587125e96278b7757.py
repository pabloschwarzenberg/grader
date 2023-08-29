minus = "abcdefghijklmnopqrstuvwxyzBDEBHIJKLMNOPQRSUVWXYZ"
s = input()
b = True
for i in s:
  if s in minus:
    b = False
    break
if b:
  print("secuencia correcta")
print("secuencia incorrecta")