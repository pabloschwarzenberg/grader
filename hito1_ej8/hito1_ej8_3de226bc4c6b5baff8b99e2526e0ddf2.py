#Descomponer un número
n=str(input())
if len(n)==1:
    print(n[0],"U")
if len(n)==2:
    print(n[0],"D +",n[1],"U")
if len(n)==3:
    print(n[0],"C +",n[1],"D +",n[2],"U")
if len(n)==4:
    print(n[0],"M +",n[1],"C +",n[2],"D +",n[3],"U")
  