#Descomponer un número
n = int(input("Ingrese un número:"))
if(len(str(n))>4):
     print("Numero demasiado largo")
else:
    if(len(str(n)) == 1):
          U = n//1
          print(U,"U")
    if(len(str(n)) == 2):
          D = n//10
          U = n%10
          print(D,"D","+",U,"U")
    if(len(str(n)) == 3):
          C = n//100
          D = (n%100)//10
          U = ((n%100)%10)
          print(C,"C","+",D,"D","+",U,"U")
    if(len(str(n)) == 4):
          M = n//1000
          C = (n%1000)//100
          D = ((n%1000)%100)//10
          U = (((n%1000)%100)%10)
          print(M,"M","+",C,"C","+",D,"D","+",U,"U")