#Contestador de celular
num = int(input("Ingrese número telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

a = (((((num % 1000000) % 1000000) % 100000) % 10000) % 1000) // 100
b = ((((((num % 1000000) % 1000000) % 100000) % 10000) % 1000) % 100) // 10
c = ((num % 1000000) % 1000000) % 10

d = (num // 1000000) // 10
e = (num % 10000000) // 1000000
f = (num % 1000000) // 100000

print(d, e, f)

if hora >= 0 and hora <= 7:
  print("CONTESTAR")

elif hora >= 7 and hora <= 14:
 if a == 9 and b == 0 and c == 9:
  print("CONTESTAR")
 else: 
  print("NO CONTESTAR")  

elif hora >= 14 and hora <= 17:
  print("NO CONTESTAR")

elif hora >= 17 and hora <= 19:
 if d == 8 and e == 7 and f == 7:
  print("NO CONTESTAR")
 else:
  print("CONTESTAR")  

elif hora >= 19 and hora <= 23:
  print("NO CONTESTAR")
      