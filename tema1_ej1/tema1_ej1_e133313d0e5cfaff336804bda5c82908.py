#Suma de los N primeros números
n=int(input("ingrese el e-nesimo numero natural" ))
s=int((n*(n+1))/(2))
if n<=0:
  input("ingrese un numero positivo" )
else:
  print(int(s))