numero = int(input('Ingrese un número de 4 dígitos: '))

if numero < 10000:
  m = numero//1000
  numero = numero - m*1000
  c = numero//100
  numero = numero - c*100
  d = numero//10
  numero = numero - d*10
  u = numero

  print(m,'M','+',c,'C','+',d,'D','+',u,'U')



  print(m,'M','+',c,'C','+',d,'D','+',u,'U')