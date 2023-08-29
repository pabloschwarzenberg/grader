#Descomponer un número
n=int(input("Ingrese número:"))
n=str(n)
if 0<=int(n)<=9:
  print(n,"U")
elif 9<int(n)<=99:
  print(n[0],"D+",n[1],"U")
elif 99<int(n)<=999:
  print(n[0],"C+",n[1],"D+",n[2],"U")
elif 999<int(n):
  print(n[0],"M+",n[1],"C+",n[2],"D+",n[3],"U")