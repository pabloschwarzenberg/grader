#Descomponer un número
a=str(input())
if(len(a)==1):
  print(str(a[0])+"U")
if(len(a)==2):
  print(str(a[0])+"D+"+str(a[1])+"U")
if(len(a)==3):
  print(str(a[0])+"C+"+str(a[1])+"D+"+str(a[2])+"U")
if(len(a)==4):
  print(str(a[0])+"M+"+str(a[1])+"C+"+str(a[2])+"D+"+str(a[3])+"U")