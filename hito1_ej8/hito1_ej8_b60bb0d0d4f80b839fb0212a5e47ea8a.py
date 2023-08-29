
numero=int(input("Numero:"))
A=int(numero/1000)
B=int((numero-A*1000)/100)
C=int((numero-A*1000-B*100)/10)
D=int(numero-A*1000-B*100-C*10)
print(A,"M+",B,"C+",C,"D+",D,"U")
  