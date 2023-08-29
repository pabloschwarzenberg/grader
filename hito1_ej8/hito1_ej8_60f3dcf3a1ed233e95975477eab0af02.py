#Descomponer un número
num = int(input("Ingresa un numero: "))
n = str(num)
co = len(n)

if co==4:
  print(n[0:1],"M +",n[1:2],"C +",n[2:3],"D +",n[3:4],"U")
elif co==3:
  print(n[0:1],"C +",n[1:2],"D +",n[2:3],"U")
elif co==2:
  print(n[0:1],"D +",n[1:2],"U")
elif co==1:
  print(n[0:1],"U")