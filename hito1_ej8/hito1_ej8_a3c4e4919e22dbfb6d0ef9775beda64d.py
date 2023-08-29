num = str(input("Ingrese un número de 4 dígitos: "))

while len(num) > 4 or int(num) < 0:
  
  print("Inválido.")
  num = str(input("Ingrese un número de 4 dígitos: "))

if len(num) == 1:

  U = str(num[0])

  print(U,"U")

elif len(num) == 2:

  U = str(num[1])
  D = str(num[0])

  print(D, "D + ", U,"U")

elif len(num) == 3:

  U = str(num[2])
  D = str(num[1])
  C = str(num[0])

  print(C,"C + ", D, "D + ", U,"U")

elif len(num) == 4:

  U = str(num[3])
  D = str(num[2])
  C = str(num[1])
  M = str(num[0])

  print(M,"M + ", C,"C + ", D, "D + ", U,"U")