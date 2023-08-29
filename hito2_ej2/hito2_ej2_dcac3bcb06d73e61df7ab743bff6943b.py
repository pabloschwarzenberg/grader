secuencia=input()
a=list(secuencia)
for i in range(len(a)):
  palabra=a[i]
  if i=="A" or i=="C" or i=="T" or i=="G" or i=="a" or i=="c" or i=="t" or i=="g":
    i=i+1
  else:
     print("secuencia incorrecta")
     break
  print("Secuencia correcta")