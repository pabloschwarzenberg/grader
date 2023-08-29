#Descomponer un número
digitos=5
while digitos>4: 
  num=int(input("ingrese un numero de hasta 4 digitos: "))
  digitos=len(str(num))
  if digitos > 4:
    print("ingrese un número de hasta 4 digitos porfavor.")
n=num
U= n%10
n=n//10
D= n%10 
n=n//10
C= n%10
n= n//10
M= n%10
n=n//10
if digitos==1:
  print(U,"U")
elif digitos==2:
  print(D,"D","+",U,"U")
elif digitos ==3:
  print(C,"C","+",D,"D","+",U,"U")
else:
  print(M,"M","+",C,"C","+",D,"D","+",U,"U")