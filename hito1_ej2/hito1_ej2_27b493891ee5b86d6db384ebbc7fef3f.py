#Contestador de celular
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese la hora de llamada: "))
termina = numero % 1000
comienza = numero // 10**5
if hora >= 0 and 0 <= 7:
 print("CONTESTAR")
if hora < 14:
 if termina == 909:
  print("CONTESTAR")
 else:
  print("NO CONTESTAR")
if hora >= 15 and hora <= 19:
 if comienza == 877:
  print("NO CONTESTAR")
 else:
  print("CONTESTAR")
if hora > 19:
 print("NO CONTESTAR")