#Contestador de celular
num = int(input("Ingrese número: "))
hora = int(input("Ingrese hora: "))

a = num//10000000
num = num%10000000
b = num//1000000
num = num%1000000
c = num//100000

num = num%100000
num = num%10000
num = num%1000

d = num

if hora<=7:
 print("CONTESTAR")

if 7<hora<=14:
 if d==909:
  print("CONTESTAR")
 else:
  print("NO CONTESTAR")

if 17<=hora<=19:
 if a==8 and b==7 and c==7:
  print("NO CONTESTAR")
 else:
  print("CONTESTAR")

if hora>=19:
 print("NO CONTESTAR")