#Contestador de celular
A = int(input("Ingrese el primer digito: "))
B = int(input("Ingrese el segundo digito: "))
C = int(input("Ingrese el tercer digito: ")) 
D = int(input("Ingrese el cuarto digito: "))
E = int(input("Ingrese el quinto digito: "))
F = int(input("Ingrese el sexto digito: "))
G = int(input("Ingrese el septimo digito: "))
H = int(input("Ingrese el octavo digito: "))
Hora = int(input("Ingrese la hora de llamado: "))
#Procedimiento
if Hora >= 0 and Hora <= 7:
  print("Contestas la llamada, pues podria ser una emergencia")
elif Hora < 14 and F == 9 and G == 0 and H == 9:
  print("Contestas la llamada")
elif Hora < 14 and F != 9 and G != 0 and H != 9:
  print("No contestas la llamada")
elif Hora >= 17 and Hora <= 19 and A != 8 and B != 7 and C != 7:
  print("No contestas la llamada")
elif Hora >= 17 and Hora <= 19 and A == 8 and B == 7 and C == 7:
  print("Contestas la llamada")
elif Hora > 19:
  print("No contestas la llamada")
else:
  print("No contestas la llamada")