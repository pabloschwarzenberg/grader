#Contestador de celular
number = int(input("Ingrese número telefónico: "))
hr = int(input("Ingrese hora de la llamada: "))

if number > 99999999 or number < 0:
  print("número inválido")
if hr > 23 or hr < 0:
  print("hora inválida")

first_3 = number//10**5
last_3 = number%10**3

if 0 <= hr <= 7:
  contestar = 1
elif 7 < hr < 14 and last_3 == 909:
  contestar = 1
elif 17 <= hr <= 19 and not first_3 == 877:
  contestar = 1
else:
  contestar = 0
  
if contestar == 1:
  print("Resultado: CONTESTAR")
else:
  print("Resultado: NO CONTESTAR")