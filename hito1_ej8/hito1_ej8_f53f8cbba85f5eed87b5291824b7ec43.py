#Descomponer un número
num=int(input("Ingrese un numero de hasta 4 digitos:"))
strnum=str(num)
if num>4:
  print('Exedio los 4 digitos')
len(strnum)
if len(strnum)==4:
  a=(strnum[0])
  b=(strnum[1])
  c=(strnum[2])
  d=(strnum[3])
  print(a,"M", "+", b,"C","+",c,"D","+",d,"U")
if len(strnum)==3:
  a=(strnum[0])
  b=(strnum[1])
  c=(strnum[2])
  print(a,"C", "+", b,"D","+",c,"U")
if len(strnum)==2:
  a=(strnum[0])
  b=(strnum[1])
  print(a,"D","+",b,"U")
if len(strnum)==1:
  a=(strnum[0])
  print(a,"U")
if len(strnum)==0:
  print("No hay numero")      