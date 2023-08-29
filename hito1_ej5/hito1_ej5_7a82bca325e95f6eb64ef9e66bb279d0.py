#Cálculo del dígito verificador de un rut
rut = int(input())
n = (rut % 10) * 2
n2 = ((rut % 100)//10) * 3
n3 = ((rut % 1000)//100) * 4
n4 = ((rut % 10000)//1000) * 5
n5 = ((rut % 100000)//10000) * 6
n6 = ((rut % 1000000)//100000) * 7
n7 = ((rut % 10000000)//1000000) * 2
n8 = ((rut % 100000000)//10000000) * 3
valor = (n + n2 + n3 + n4 + n5 + n6 + n7 + n8)
valor1 = valor // 11
valor2 = valor - (11 * valor1)
valor3 = 11 - valor2
if valor3 == 11:
  print("dv=",0)
elif valor3 == 10:
  print("dv=","K")
elif valor3 < 10:
  print("dv=",valor3)          