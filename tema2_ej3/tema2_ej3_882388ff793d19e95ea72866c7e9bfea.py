def numero_perfecto(a):
  suma=0
  for i in range(1,a):
    if(a%i==0):
      suma+=i

  if a==suma:
    return True
  else:
    return False

a=int(input("ingrese un numero:"))

if numero_perfecto(a):
  print("es perfecto")
else:
  print("no es perfecto")