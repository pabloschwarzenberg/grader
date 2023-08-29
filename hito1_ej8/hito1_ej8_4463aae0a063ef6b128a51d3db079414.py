#Descomponer un número
n=str(input("Ingrese un número de hasta 4 dígitos: "))
if(len(n)==1):
  print(n[0],"U",sep="")
if(len(n)==2):
  print(n[0],"D + ",n[1],"U",sep="")
if(len(n)==3):
  print(n[0],"C + ",n[1],"D + ",n[2],"U",sep="")
if(len(n)==4):
  print(n[0],"M + ",n[1],"C + ",n[2],"D + ",n[3],"U",sep="")