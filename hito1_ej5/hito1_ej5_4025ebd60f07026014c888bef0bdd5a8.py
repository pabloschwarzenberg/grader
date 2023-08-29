#Cálculo del dígito verificador de un rut
rut = eval(input("ingrese rut sin dv: "))
n1 = rut % 10
n2 = (rut % 100 - n1)//10
n3 = (rut % 1000 - n2)//100
n4 = (rut % 10000 - n3)//1000
n5 = (rut % 100000 - n4)//10000
n6 = (rut % 1000000 - n5)//100000
n7 = (rut % 10000000 - n6)//1000000
n8 = (rut % 100000000 - n7)//1000000 // 10

digitos = (n1*2)+(n2*3)+(n3*4)+(n4*5)+(n5*6)+(n6*7)+(n7*2)+(n8*3)
resto = digitos % 11
resultado = 11 - resto

if resultado == 11:
  print("dv = 0")
elif resultado == 10:
  print("dv = k")
else:
  print("dv = ", resultado)