#Descomponer un número
N=input("Ingrese un número: ")
A=N[:1]
V=N[1:2]
C=N[2:3]
D=N[3:4]
N=int(N)
if N>999:
  print(A,"M","+",V,"C","+",C,"D","+",D,"U")
else:
  if 99<N<1000:
    print(A,"C","+",V,"D","+",C,"U")
  else:
    if 9<N<100:
      print(A,"D","+",V,"U")
    else:
      if N<10:
        print(A,"U")      