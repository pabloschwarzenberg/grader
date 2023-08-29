n = input("numero:")
N = int(n)

M1 = N // 1000

C1 = N % 1000
C2 =int(C1 // 100)

D1 = N % 100
D2 = int(D1 //10)

U1 = N % 10
U2 =int(U1 // 1)

if len (n) == 4:
  print(M1,"M +",C2,"C +",D2,"D +",U2,"U")

elif len(n) == 3:
  print(C2,"C +",D2,"D +",U2,"U")

elif len (n) ==2:
  print(D2,"D +",U2,"U")

elif len (n) == 1:
  print(U2,"U")
  
  
      