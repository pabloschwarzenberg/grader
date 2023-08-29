n = str(input())
j = n.lower()
def validacion(a):
  h = []
  b = "atgc"
  x = (x for j in b)
  for i in a:
    if i == "a":
        pass
    elif i == "c":
        pass
    elif i == "t":
        pass
    elif i == "g":
      pass
    else:
      h.append(0)
    h.append(1)
  return h
if 0 in validacion(j):
  print("secuencia incorrecta")
else:
  print("secuencia correcta")
