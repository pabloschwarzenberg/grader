#Descomponer un número
num = input()

if len(num) == 4:
  print('{}M + {}C + {}D + {}U'.format(*num))
if len(num) == 3:
  print('{}C + {}D + {}U'.format(*num))
if len(num) == 2:
  print('{}D + {}U'.format(*num))
if len(num) == 1:
  print('{}U'.format(num))