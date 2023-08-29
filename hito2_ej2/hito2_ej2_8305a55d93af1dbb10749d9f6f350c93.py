def secuencia(a):  
  for i in range(len(a)):
      noson=0
      if a[i] not in "actg":
          noson=noson+1
  if noson != 0:
    print("secuencia incorrecta")
  if noson == 0:
    print("secuencia correcta")
 
se=input("Ingrese secuencia: ")
a=se.lower()
print(secuencia(a))
