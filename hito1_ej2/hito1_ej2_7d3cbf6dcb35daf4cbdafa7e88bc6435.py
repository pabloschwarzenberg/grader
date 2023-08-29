Num = input("Numero de llamada: ")
Hora = int(input('Hora de llamada: '))
if 0<=Hora<=7:
  print('CONTESTAR')
elif(7<Hora<=14) and int(Num[5:])!= 909:
  print('NO CONTESTAR')
elif(7<Hora<=14) and int(Num[5:])== 909:
  print('CONTESTAR')
elif(17<=Hora<19) and (int(Num[:3])!= 877):
  print('CONTESTAR')
elif (17<=Hora<19) and (int((Num[:3]))== 877):
  print('NO CONTESTAR')
elif 19<=Hora:
  print('NO CONTESTAR')