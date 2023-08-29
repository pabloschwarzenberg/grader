#Descomponer un número
a=int(input("Ingrese un nuemor: "))
if(9999>=a>=1000):
  M=((a%10000)//1000)
  C=((a%1000)//100)
  D=((a%100)//10)
  U=((a%10)//1)
  print(M,"M +", C,"C +", D,"D +", U,"U")
elif(999>=a>=100):
  C=((a%1000)//100)
  D=((a%100)//10)
  U=((a%10)//1)
  print(C,"C +", D,"D +", U,"U")
elif(99>=a>=10):
  D=((a%100)//10)
  U=((a%10)//1)
  print(D,"D +", U,"U")
else:
  U=(a%10)
  print(U,"U")