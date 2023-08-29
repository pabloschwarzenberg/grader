n=input("Ingrese el número a descomponer: ")
l=len(n)
if l<2:
  u=n[l-1]
  print(u,"U")
elif l<3:
  u=n[l-1]
  d=n[l-2]
  print(d,"D + ",u,"U")
elif l<4:
  u=n[l-1]
  d=n[l-2]
  c=n[l-3]
  print(c,"C + ",d,"D + ",u,"U")
elif l<5:
  u=n[l-1]
  d=n[l-2]
  c=n[l-3]
  m=n[l-4]
  print(m,"M + ",c,"C + ",d,"D + ",u,"U")
else:
  print("Ingrese un número de máximo 4 digitos")