#Descomponer un número
n=input("numero")
length=len(n)
if length==1:
  print(n+"U")
elif length==2:
  print(n[0]+"D + "+n[1]+"U")
elif length==3:
  print(n[0]+"C + "+n[1]+"D + "+n[2]+"U")
else:
  print(n[0]+"M + "+n[1]+"C + "+n[2]+"D + "+n[3]+"U")