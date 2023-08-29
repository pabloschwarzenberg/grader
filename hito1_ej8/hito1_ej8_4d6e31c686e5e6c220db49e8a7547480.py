#Descomponer un número
n=str(input())
n1=len(n)
if n1==4:
  print(n[0]+"M+"+n[1]+"C+"+n[2]+"D+"+n[3]+"U")
if n1==3:
  print(n[0]+"C+"+n[1]+"D+"+n[2]+"U")
if n1==2:
  print(n[0]+"D+"+n[1]+"U")
if n1==1:
  print(n[0]+"U")
 