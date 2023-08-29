#Descomponer un número
n=int(input())
if 1000<=n<=9999:
    M=n//1000
    C=(n-(M*1000))//100
    D=(n-(M*1000)-(C*100))//10
    U=(n-(M*1000)-(C*100)-(D*10))
    print(M,"M +",C,"C +",D,"D +",U,"U")
else:
  if 100<=n<=999:
    C_1=n//100
    D_1=(n-(C_1*100))//10
    U_1=(n-(C_1*100)-(D_1*10))
    print(C_1,"C +",D_1,"D +",U_1,"U")
  else:
    if 10<=n<=99:
      D_2=n//10
      U_2=(n-(D_2*10))
      print(D_2,"D +",U_2,"U")
    else:
      if 1<=n<=9:
        U_3=n
        print(n)
    