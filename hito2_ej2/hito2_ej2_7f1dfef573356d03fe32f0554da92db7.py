x = str(input())
x = list(x)
for i in range(len(x)):
  if x[i] != "A" or x[i] != "C" or x[i] != "T" or x[i] != "G" :
    print("secuencia incorrecta")
  else :
    print("secuencia correcta")