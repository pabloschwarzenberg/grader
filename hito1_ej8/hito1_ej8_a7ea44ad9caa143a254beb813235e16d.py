#Descomponer un número
nro=int(input("Ingresa un numero de 4 cifras: "))
U=nro%10
D=int((nro%100-U)/10)
C=int((nro%1000-U)/100)
M=int((nro%10000-U)/1000)
if(nro>999):
  print(M,"M","+",C,"C","+",D,"D","+",U,"U")
elif(nro>99):
  print(C,"C","+",D,"D","+",U,"U")
elif(nro>9):
  print(D,"D","+",U,"U")
elif(nro<=9):
  print(U,"U")
  