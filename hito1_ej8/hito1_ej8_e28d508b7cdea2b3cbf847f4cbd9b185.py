#Descomponer un número
N=str(input())

if len(N)==4 :
  print(N[0],"M +",N[1],"C +",N[2],"D +", N[3],"U")
if len(N)==3 :
  print(N[0],"C +",N[1],"D +", N[2],"U")
if len(N)==2 :
  print(N[0],"D +", N[1],"U")
if len(N)==1 :
  print(N[0],"U")