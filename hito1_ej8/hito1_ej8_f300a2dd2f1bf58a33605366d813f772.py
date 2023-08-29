#Descomponer un número
n=int(input())
unidades=(n%(n//10))
a=n-(n//10)*10
b=n-(n//100)*100-a
c=n-(n//1000)*1000-b-a

U=(n-(n//10)*10)
D=((n-(n//100)*100-a)//10)
C=((n-(n//1000)*1000-b-a)//100)
M=((n-(n//10000)*10000-b-a-c)//1000) 
if M>0:
  print(str(M)+"M" + "+" +str(C)+"C" + "+" + str(D)+"D" + "+" + str(U)+"U")
elif C>0:
  print(str(C)+"C" + "+" + str(D)+"D" + "+" + str(U)+"U")
elif D>0:
  print(str(D)+"D" + "+" + str(U)+"U")