#Descomponer un número
numero = str(input("Numero: "))
n1 = numero
n = len(list(str(numero)))
if n == 4:
  M = int(list(n1)[0])
  C = int(list(n1)[1])
  D = int(list(n1)[2])
  U = int(list(n1)[3])
  print (M,"M+",C,"C+",D,"D+",U,"U")
if n == 3:
  C = int(list(n1)[0])
  D = int(list(n1)[1])
  U = int(list(n1)[2])
  print (C,"C+",D,"D+",U,"U")
if n == 2:
  D = int(list(n1)[0])
  U = int(list(n1)[1])
  print (D,"D+",U,"U")
if n == 1:
  U = int(list(n1)[0])
  print ((U),"U")