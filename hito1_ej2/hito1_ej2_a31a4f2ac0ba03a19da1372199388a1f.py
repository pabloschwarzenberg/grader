#Contestador de celular

numb = int(input())
hora = int(input())

uno = numb % 10000000
dos = (numb % 10000000) % 1000000
tres = ((numb % 10000000) % 1000000) % 100000
cuatro = (((numb % 10000000) % 1000000) % 100000) % 1000
numerocentena = ((((numb % 10000000) % 1000000) % 100000) % 1000) % 100

primero = numb // 10000000
segundo = (numb % 10000000) // 1000000
tercero = ((numb % 10000000) % 1000000) // 100000

c = (((((numb % 10000000) % 1000000) % 100000) % 1000) // 100)
d = ((((((numb % 10000000) % 1000000) % 100000) % 1000) % 100) % 100) // 10
u = ((((((numb % 10000000) % 1000000) % 100000) % 1000) % 100) % 100) % 10

if hora >= 0 and hora <= 7:
 print("CONTESTAR")

if hora > 7 and hora < 14:
 if c == 9 and d == 0 and u == 9:
  print("CONTESTAR")
 else:
  print("NO CONTESTAR")

if hora >= 14 and hora <= 17:
 print("NO CONTESTAR")
    
if hora > 17 and hora < 19:
 if primero == 8 and segundo == 7 and tercero == 7:
  print("NO CONTESTAR")
 else:
  print("CONTESTAR")

if hora >= 19 and hora < 23:
 print("NO CONTESTAR")