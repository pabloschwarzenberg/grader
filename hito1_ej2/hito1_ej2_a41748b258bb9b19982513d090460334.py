#Contestador de celular
N = int(input('Ingrese número telefónico: '))
H = int(input('Ingrese hora de llamada: '))
N_str= str(N)
if 0 <= H <= 7:
 print('CONTESTAR')
elif 7 < H < 14:
 if N_str[5:8] == '909':
  print('CONTESTAR')
 else:
  print('NO CONTESTAR')
elif 17 <= H <= 19:
 if N_str[0:3] == '877':
  print('NO CONTESTAR')
 else:
  print('CONTESTAR')
elif H > 19:
 print('NO CONTESTAR')