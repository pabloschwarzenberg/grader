#Contestador de celular
import math
num = int(input("Ingrese su número: "))
hor = int(input("Ingrese hora: "))

dig = (num % 1000)
dig2 = ((num-(num % 100000))/100000)

#Pimera parte
if hor < 8:
  print("CONTESTAR")
#Segunda parte
if dig == 909 and hor > 7 and hor < 14:
  print("CONTESTAR")
if hor > 7 and hor < 14 and dig != 909:
  print("NO CONTESTAR")
#Tercera parte
if hor >= 17 and hor <= 19 and dig2 != 877:
  print("NO CONTESTAR")
if hor >= 17 and hor <= 19 and dig2 == 877:
  print("NO CONTESTAR")
if hor >= 19:
   print("NO CONTESTAR")