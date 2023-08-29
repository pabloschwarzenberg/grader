#Contestador de celular
num = int(input("Ingrese numero que llama: "))
hor = eval(input("Ingrese hora: "))

Ld = num%1000
fg = num//100000

if 0<=hor<=7:
  print("CONTESTAR")
if hor > 19:
  print("NO CONTESTAR")
if fg==877 and 17<=hor<=19:
  print("NO CONTESTAR")
if fg != 877 and 17<=hor<=19:
  print("CONTESTAR")
if hor < 14 and Ld == 909:
  print("CONTESTAR")
if hor < 14 and Ld != 909:
  print("NO CONTESTAR")
 