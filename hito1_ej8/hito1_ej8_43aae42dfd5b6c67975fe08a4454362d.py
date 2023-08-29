#Descomponer un número
n=input()
x=len(str(n))
if x==1:
  print(n[0]+"U")
if x==2:
  print(n[0]+"D","+",n[1]+"U")
if x==3:
  print(n[0]+"C","+",n[1]+"D","+",n[2]+"U")
if x==4:
  print(n[0]+"M","+",n[1]+"C","+",n[2]+"D","+",n[3]+"U")