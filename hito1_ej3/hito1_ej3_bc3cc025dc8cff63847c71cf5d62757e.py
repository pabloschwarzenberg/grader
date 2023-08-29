#Aprobación de créditos
ing = int(input())
nacimiento = input()
hijos = int(input())
anios = int(input())
estado = input()
camp = input()

if anios > 10 and hijos >= 2 or estado == 'C' and hijos > 3 and anios >= 45 and anios <= 55 or ing > 2500000 and estado == 'S'and camp == 'U' or ing > 350000 and anios > 5 or camp == 'R' and estado == "C" and hijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')