#Cálculo del dígito verificador de un rut
print('Ingrese número')
n = input(':')
dv = ''
n8 = int(n[7:])
n7 = int(n[6:7])
n6 = int(n[5:6])
n5 = int(n[4:5])
n4 = int(n[3:4])
n3 = int(n[2:3])
n2 = int(n[1:2])
n1 = int(n[0:1])
if n != 0:
  s1 = n8 * 2
  s2 = n7 * 3
  s3 = n6 * 4
  s4 = n5 * 5
  s5 = n4 * 6
  s6 = n3 * 7
  s7 = n2 * 2
  s8 = n1 * 3
  t = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
  t1 = t // 11
  t2 = t -(11 * t1)
  t3 = 11 - t2
  if t3 > 10:
    dv = '0'
  elif t3 == 10:
    dv = 'K'
  else:
    dv == t3
  print(dv) 