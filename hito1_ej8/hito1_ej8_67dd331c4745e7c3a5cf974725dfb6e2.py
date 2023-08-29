n = int(input("Ingrese un numero de hasta 4 digitos: "))

n1 =list(str(n))

if n1[:9]:
  print(n1[0]+"M","+",n1[1]+"C","+",n1[2]+"D","+",n1[3]+"U")
elif n1[:2]:
  print(n1[0]+"C","+",n1[1]+"D","+",n1[2]+"U")
elif n1[:1]:
  print(n1[0]+"D","+",n1[1]+"U")
elif n1[:0]:
  print(n1[0]+"U")