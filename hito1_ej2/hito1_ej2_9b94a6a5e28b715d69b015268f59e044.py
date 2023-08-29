#Contestador de celular
print("que numero le esta llamando?")
telefono = int(input())
ultimos_digitos = telefono % 1000
primeros_digitos = telefono // 100000
print("a que hora le estan llamando?")
hora = int(input())
if hora >= 0 and hora <= 7:
  print("CONTESTAR")
elif hora >= 8 and hora <= 14 and ultimos_digitos == 909:
  print("CONTESTAR")
elif hora >= 17 and hora <= 19 and primeros_digitos != 877:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")      