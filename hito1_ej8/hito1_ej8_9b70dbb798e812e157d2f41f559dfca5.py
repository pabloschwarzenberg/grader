#Descomponer un número
a=input("escribe un numero de 4 digitos: ")
if len(a)==4:
  b=a[0]
  c=a[1]
  d=a[2]
  e=a[3]
  print(b,"M +",c,"C +",d,"D +",e,"U")
if len(a)==3:
  b=a[0]
  c=a[1]
  d=a[2]
  print(b,"C +",c,"D +",d,"U")
if len(a)==2:
  b=a[0]
  c=a[1]
  print(b,"D +",c,"U")
if len(a)==1:
  b=a[0]
  print(b,"U")   