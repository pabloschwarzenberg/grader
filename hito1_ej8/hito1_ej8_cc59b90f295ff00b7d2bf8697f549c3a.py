#Descomponer un número
num =str(input("ingresar un numero de hasta 4 digitos:"))

if len(num) == 4:
  M=num[0]
  C=num[1]
  D=num[2]
  U=num[3]
  print("Para",num,"debe imprimir:",M,"M + ",C,"C + ",D,"D + ",U,"U")
elif len(num) == 3:
  C=num[0]
  D=num[1]
  U=num[2]
  print("Para",num,"debe imprimir:",C,"C + ",D,"D + ",U,"U")
elif len(num) == 2:
  D=num[0]
  U=num[1]
  print("Para",num,"debe imprimir:",D,"D + ",U,"U")
elif len(num) == 1:
  U=num[0]
  print("Para",num,"debe imprimir:",U,"U")