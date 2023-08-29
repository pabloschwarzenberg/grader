#Cálculo del dígito verificador de un rut
rut=int(input("ingresa tu rut: "))
rut_str = str(rut)
rut_lista = list(rut_str)
numero_8 = int(99999999)
numero_7 = int(9999999)
rut_int = int(rut)

x = int(rut_lista[-1]) *  2
x2 = int(rut_lista[-2]) * 3
x3 = int(rut_lista[-3]) * 4
x4 = int(rut_lista[-4]) * 5
x5 = int(rut_lista[-5]) * 6
x6 = int(rut_lista[-6]) * 7
x7 = int(rut_lista[-7]) * 2


if rut_int > 9999999 and rut_int > 0:
  x8 = x8 = int(rut_lista[0]) * 3 
elif rut_int > 999999:
  x8 = 0


suma = int(x + x2 + x3 +x4 + x5 + x6 +x7 + (x8))

division = (suma // 11)
multiplicacion = (11 * division)
a = suma - multiplicacion
total = 11 - a


if total == 11:
  print("dv=0")
elif total == 10:
  print("dv=K")
elif 9 >= total >= 1 :
  print("dv=",total)
else:
  print("no valido")     