#Contestador de celular
num = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de llamada: "))

final = num%1000
inicio = num//10000

if 0 <= hora <= 7 or 7 < hora <= 14 and final == 909 or 17 <= hora <= 19 and inicio == 877:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")
