#Cálculo del dígito verificador de un rut
Rut = eval(input("Ingrse su rut sin el numero despues de guion : "))
x1 = (Rut//1)%10
x2 = (Rut//10)%10
x3 = (Rut//100)%10
x4 = (Rut//1000)%10
x5 = (Rut//10000)%10
x6 = (Rut//100000)%10
x7 = (Rut//1000000)%10
x8 = (Rut//10000000)%10

#mult por el patron
p1 = x1 * 2
p2 = x2 * 3
p3 = x3 * 4
p4 = x4 * 5
p5 = x5 * 6
p6 = x6 * 7
p7 = x7 * 2
p8 = x8 * 3

#suma
suma = p1 + p2 + p3 + p4 + p5 + p6 + p7 +p8

#numero verificador
resta = suma%11
verificador = 11 - resta

if verificador ==10:
  print("dv=k")
elif resta == 0:
  print("dv=0")
else:
  print("dv="+str(verificador))